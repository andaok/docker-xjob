# -*- encoding:utf-8 -*-
#--------------------------------
# @Date    : 2017-05-10 15:00
# @Author  : itwye
# @Email   : itwye@qq.com
# @Version : v1.6
# @Desrc   : job url router
# -------------------------------- 

from django.conf.urls import url
from jobapp import views

app_name = "jobapp"

urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^get_app_info/$',views.get_appinfo_from_bking,name="get_app_info"),
    url(r'^get_set_info/$',views.get_setinfo_from_bking,name="get_set_info"),
    url(r'^get_module_info/$',views.get_moduleinfo_from_bking,name="get_module_info"),
    url(r'^target_hosts_info/$',views.target_hosts_info,name="target_hosts_info"),
    url(r'^get_host_detail_info/$',views.get_host_detail_info,name="get_host_detail_info"),
    url(r'^login/$',views.auth_login,name="login"),
    url(r'^login1/$',views.auth_login_new,name="login_new"),
    url(r'^logout/$',views.auth_logout,name="logout"),
    url(r'^get_failure_task_detail_info/$',views.get_failure_task_detail_info,name="get_failure_task_detail_info"),
    url(r'^state_sls_job_execute/$',views.state_sls_job_execute,name="state_sls_job_execute"),
    url(r'^get_job_hosts_task_status/$',views.get_job_hosts_task_status,name="get_job_hosts_task_status"),
    url(r'^get_job_host_task_info/$',views.get_job_host_task_info,name="get_job_host_task_info"),
    url(r'^hostname_base_bking_module/$',views.hostname_base_bking_module,name="hostname_base_bking_module"),
    url(r'^dynamicgroup/manage/$',views.dynamic_group_manage,name="dynamic_group_manage"),
    url(r'^dynamicgroup/show/$',views.dynamic_group_records,name="dynamic_group_show"),
    url(r'^dynamicgroup/get/id/$',views.dynamic_group_record_by_id,name="dynamic_group_record_by_id"),
    url(r'^dynamicgroup/del/id/$',views.dynamic_group_del_record_by_id,name="dynamic_group_del_record_by_id"),
    url(r'^dynamic_group_hosts_info/$',views.dynamic_group_hosts_info,name="dynamic_group_hosts_info"),
    url(r'^saltgroup/manage/$',views.salt_group_manage,name="salt_group_manage"),
    url(r'^saltgroup/all/$',views.salt_group_all,name="salt_group_all"),
    url(r'^saltgroup/get/id/$',views.salt_group_record_by_id,name="salt_group_record_by_id"),
    url(r'^saltgroup/del/id/$',views.salt_group_del_record_by_id,name="salt_group_del_record_by_id"),
    url(r'^salt_group_hosts_info/$',views.salt_group_hosts_info,name="salt_group_hosts_info"),
    url(r'^cmd_run_job_execute/$',views.cmd_run_job_execute,name="cmd_run_job_execute"),
    url(r'^cmd_script_job_execute/$',views.cmd_script_job_execute,name="cmd_script_job_execute"),
    url(r'^upload_file_job_execute/$',views.upload_file_job_execute,name="upload_file_job_execute"),
    url(r'^upload/$',views.upload,name="upload"),
    url(r'^user/files/show/$',views.user_dir_files_list,name="user_files_show"),
    url(r'^get_upload_job_hosts_task_status/$',views.get_upload_job_hosts_task_status,name="get_upload_job_hosts_task_status"),
    url(r'^get_upload_file_progress/$',views.get_upload_file_progress,name="get_upload_file_progress"),
    url(r'^get_script_job_hosts_task_status/$',views.get_script_job_hosts_task_status,name="get_script_job_hosts_task_status"),
    url(r'^audit/$',views.audit,name="audit"),
    url(r'^help/$',views.help,name="help"),
    url(r'^del_file/$',views.del_file,name="del_file"),
    url(r'^shortcut_search_host/$',views.shortcut_search_host,name="shortcut_search_host"),
    url(r'^execuser/name/show/$',views.execuser_name_list,name="execuser_name_show"),
    url(r'^get/customscript/args/$',views.get_script_args,name="get_script_args"),
    url(r'^show/customscript/(?P<page>[\w\-]+)/$',views.get_custom_script_list,name="show_custom_script"),
    url(r'^systemuser/manage/(?P<page>[\w\-]+)/$',views.get_system_user_list,name="system_user_manage"),
    url(r'^systemuser/save/$',views.system_user_save,name="system_user_save"),
    url(r'^systemuser/del/$',views.system_user_del,name="system_user_del"),
    url(r'^create/customscript/$',views.create_custom_script,name="create_custom_script"),
    url(r'^edit/customscript/(?P<id>[\w\-]+)/$',views.edit_custom_script,name="edit_custom_script"),
    url(r'^all/customscript/$',views.custom_scripts_all,name="custom_scripts_all"),
    url(r'^save/customscript/$',views.save_custom_script,name="save_custom_script"),
    url(r'^del/customscript/$',views.del_custom_script,name="del_custom_script"),
]
