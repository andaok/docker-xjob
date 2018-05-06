#!/bin/bash

# Author: itwye
# Email : itwye@qq.com
# Date  : 20180506  

# Initialization System

function initSys() 
{
    # Generate configuration file by environment variable

    # Salt master configuration

    sed -i "s/#mysql_host#/${MYSQL_HOST}/g" /etc/salt/master
    sed -i "s/#mysql_user#/${MYSQL_USER}/g" /etc/salt/master
    sed -i "s/#mysql_user_password#/${MYSQL_USER_PASSWORD}/g" /etc/salt/master
    sed -i "s/#mysql_salt_database#/${MYSQL_SALT_DATABASE}/g" /etc/salt/master

    # Django setting

    sed -i "s/#mysql_host#/${MYSQL_HOST}/g" /job/django_cmdb_project/django_cmdb_project/settings.py
    sed -i "s/#mysql_user#/${MYSQL_USER}/g" /job/django_cmdb_project/django_cmdb_project/settings.py
    sed -i "s/#mysql_user_password#/${MYSQL_USER_PASSWORD}/g" /job/django_cmdb_project/django_cmdb_project/settings.py
    sed -i "s/#mysql_job_database#/${MYSQL_JOB_DATABASE}/g" /job/django_cmdb_project/django_cmdb_project/settings.py

    # Job view.py

    sed -i "s/#mysql_host#/${MYSQL_HOST}/g" /job/django_cmdb_project/jobapp/views.py
    sed -i "s/#mysql_user#/${MYSQL_USER}/g" /job/django_cmdb_project/jobapp/views.py
    sed -i "s/#mysql_user_password#/${MYSQL_USER_PASSWORD}/g" /job/django_cmdb_project/jobapp/views.py
    sed -i "s/#mysql_salt_database#/${MYSQL_SALT_DATABASE}/g" /job/django_cmdb_project/jobapp/views.py

    # Prepare directory

    mkdir -p /srv/salt/scripts
    mkdir -p /srv/salt/upload_files

    LOOP="YES"
    TIMECOUNT=0

    while [ "$LOOP" == "YES" ]
      do
          mysql -h${MYSQL_HOST} -u${MYSQL_USER} -p${MYSQL_USER_PASSWORD} -e "use ${MYSQL_JOB_DATABASE}"

          if [ $? != 0 ]; then
              sleep 2
              let TIMECOUNT=TIMECOUNT+2
              if [ "$TIMECOUNT" -ge "30" ]; then
                  echo "--- ${MYSQL_HOST} may be startup failed! ---"
                  LOOP="NO"
              fi
          else
              # Initialization job database
              python /job/django_cmdb_project/manage.py makemigrations
              python /job/django_cmdb_project/manage.py migrate
              # Create django superuser
              printf "from django.contrib.auth.models import User\nif not User.objects.exists(): User.objects.create_superuser(*'$DJANGO_SUPER_USER'.split(':'))" | python /job/django_cmdb_project/manage.py shell

              LOOP="NO"
          fi
      done

}


if [ ! -f "/var/run/init.flag" ]; then
    initSys
    if [ $? == 0 ]; then
       touch /var/run/init.flag
       echo "--- ${MYSQL_JOB_DATABASE} Initialization success!!! ---"
    else
       echo "--- ${MYSQL_JOB_DATABASE} may be Initialization failed! ---"     
    fi     
fi


# Start the first process
/usr/bin/salt-master -d
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start salt-master: $status"
  exit $status
fi

# Start the second process
nohup python /job/django_cmdb_project/manage.py  runserver 0.0.0.0:8000 &
status=$?
if [ $status -ne 0 ]; then
  echo "Failed to start django : $status"
  exit $status
fi


while sleep 60; do
  ps aux | grep salt-master | grep -q -v grep
  PROCESS_1_STATUS=$?
  ps aux | grep cmdb | grep -q -v grep
  PROCESS_2_STATUS=$?
  # If the greps above find anything, they exit with 0 status
  # If they are not both 0, then something is wrong
  if [ $PROCESS_1_STATUS -ne 0 -o $PROCESS_2_STATUS -ne 0 ]; then
    echo "One of the processes has already exited."
    exit 1
  fi
done
