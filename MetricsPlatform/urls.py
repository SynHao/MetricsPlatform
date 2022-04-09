"""MetricsPlatform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from MetricsModel import views
from Sql import views as sql_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('meta/', views.meta),





    path('metric_list', views.metric_list),
    path('business_type', views.business_type),
    path('metric_type', views.metric_field),
    path('time_cycle', views.time_cycle),
    path('dim_list', views.dim_list),
    path('dim_value_list', views.dim_value_list),



    path('api/rest_j/v1/dss/framework/workspace/getWorkspaceBaseInfo', views.getWorkspaceBaseInfo),
    path('api/rest_j/v1/dss/framework/workspace/getBaseInfo', views.getBaseInfo),
    path('api/rest_j/v1/dss/framework/workspace/workspaces', views.getWorkspaces),
    path('api/rest_j/v1/dss/framework/workspace/workspaces/224/applications', views.getWorkspacesIDApplications),
    path('api/rest_j/v1/datasource/all', views.getDatasourceAll),
    path('api/rest_j/v1/udf/all', views.getUDFAll),
    path('api/rest_j/v1/filesystem/getUserRootPath', views.getUserRootPath),
    path('api/rest_j/v1/jobhistory/list', views.getJobHistoryList),
    path('api/rest_j/v1/syn/workspaces/demos', views.getDemos),
    path('api/rest_j/v1/syn/workspaces/videos', views.getVideos),
    path('api/rest_j/v1/syn/workspaces/departments', views.getDepartments),
    path('api/rest_j/v1/syn/workspaces/9', views.getWorkspacesID),
    path('api/rest_j/v1/dss/workspaces/9/favorites', views.getWorkspacesIDFavorites),
    path('api/rest_j/v1/dss/workspaces/9/managements', views.getWorkspacesIDManagements),
    path('api/rest_j/v1/filesystem/getDirFileTrees', views.getDirFileTrees),

    # re_path(r'^sql.*/?$', sql_views.hue, name='sql_views_hue'),
]
