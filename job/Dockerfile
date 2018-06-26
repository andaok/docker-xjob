# 
# saltstack and django container 
#

FROM ubuntu:14.04
MAINTAINER itwye<itwye@qq.com>

COPY sources.list /etc/apt/sources.list
RUN mkdir /root/.pip/
COPY pip.conf /root/.pip/pip.conf

RUN apt-get update \ 
    && apt-get install -y wget python-pip python-dev mysql-client libldap2-dev libsasl2-dev libmysqlclient-dev \
    && wget -O - http://repo.saltstack.com/apt/ubuntu/14.04/amd64/archive/2017.7.4/SALTSTACK-GPG-KEY.pub | sudo apt-key add - \
    && echo "deb http://repo.saltstack.com/apt/ubuntu/14.04/amd64/archive/2017.7.4 trusty main" >> /etc/apt/sources.list.d/saltstack.list \
    && apt-get update \
    && pip install --upgrade pip \
    && pip install django==1.11 \
    && pip install python-ldap==3.0.0 \
    && pip install django-auth-ldap==1.5.0 \
    && pip install mysql-python \
    && apt-get install -y salt-master \
    && mkdir -p /srv/salt \
    && mkdir -p /job \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

COPY SaltMaster.conf /etc/salt/master
COPY django_cmdb_project /job/django_cmdb_project 
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

VOLUME ["/etc/salt/pki", "/var/cache/salt", "/var/log/salt", "/etc/salt/master.d", "/srv/salt"]
EXPOSE 4505 4506 8000

CMD "/startup.sh"

