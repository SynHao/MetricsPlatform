from django.http import JsonResponse, QueryDict
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from MetricsModel.factory.status_code import StatusCode
from MetricsModel.models import MetricList, MetaInfoModel
from MetricsModel.serializers import MetricListSerializer, MetaInfoSerializer


@csrf_exempt
def metric_list(request):
    metrics = MetricList.objects.all()
    serializer = MetricListSerializer(metrics, many=True)
    return_data = {
        "data": {
            "list": serializer.data
        }
    }
    return JsonResponse(return_data, safe=False)


def get_meta_info(type=MetaInfoModel.MetaType, value=None):
    """
    获取元数据信息
    :param value: 维度值信息
    :arg type 元数据类型
    """
    if type == MetaInfoModel.MetaType.dim_value:
        parent = MetaInfoModel.objects.get(type=MetaInfoModel.MetaType.dim, value=value)
        meta_business = MetaInfoModel.objects.filter(type=type, parent_id=parent.id)
        serializer = MetaInfoSerializer(meta_business, many=True)
        data = serializer.data
        for d in data:
            d['parent'] = value
    else:
        meta_business = MetaInfoModel.objects.filter(type=type)
        serializer = MetaInfoSerializer(meta_business, many=True)
        data = serializer.data
    return JsonResponse({
        "data": {
            "list": data
        },
        "status": StatusCode.success,
        "message": "OK",
    })


def meta(request):
    type = request.GET.get("type")
    if type == "business":
        return get_meta_info(MetaInfoModel.MetaType.business)
    elif type == "metrics":
        return get_meta_info(MetaInfoModel.MetaType.metrics)
    elif type == "time_cycle":
        return get_meta_info(MetaInfoModel.MetaType.time_cycle)
    elif type == "dim":
        return get_meta_info(MetaInfoModel.MetaType.dim)
    elif type == "dim_value":
        value = request.GET.get("value")
        return get_meta_info(MetaInfoModel.MetaType.dim_value, value)
    return JsonResponse({
        "data": {
            "list": [{
                'key': 'basic',
                'value': '基础'
            }, {
                'key': 'ssp',
                'value': 'SSP'
            }, {
                'key': 'md',
                'value': '聚合'
            }]
        }
    })


@csrf_exempt
def business_type(request):
    return JsonResponse({
        "data": {
            "list": [{
                'key': 'basic',
                'value': '基础'
            }, {
                'key': 'ssp',
                'value': 'SSP'
            }, {
                'key': 'md',
                'value': '聚合'
            }]
        }
    })


@csrf_exempt
def metric_field(request):
    return JsonResponse({
        "data": {
            "list": [{
                'key': 'req_cnt',
                'value': '请求次数'
            }, {
                'key': 'req_dev',
                'value': '请求设备数'
            }, {
                'key': 'rdt_cnt',
                'value': '转发次数'
            }]
        }
    })


@csrf_exempt
def time_cycle(request):
    return JsonResponse({
        "data": {
            "list": [{
                'key': 'd',
                'value': '每日'
            }, {
                'key': '1d',
                'value': '次日'
            }, {
                'key': '1w',
                'value': '7日'
            }]
        }
    })


@csrf_exempt
def dim_list(request):
    return JsonResponse({
        "data": {
            "list": [{
                'key': 'status',
                'value': '业务状态'
            }, {
                'key': 'dim_type',
                'value': '维度修饰类型'
            }, {
                'key': 'event_type',
                'value': '事件名称'
            }]
        }
    })


@csrf_exempt
def dim_value_list(request):
    dim_key = request.GET.get('dim_key')
    if dim_key == 'status':
        return JsonResponse({
            "data": {
                "list": [{
                    'key': '001',
                    'value': '有效'
                }, {
                    'key': '002',
                    'value': '成功',
                }]
            }
        })
    else:
        return JsonResponse({
            "data": {
                "list": [{
                    'key': '001',
                    'value': '展示'
                }, {
                    'key': '002',
                    'value': '点击'
                }, {
                    'key': '003',
                    'value': '下载'
                }]
            }
        })


@csrf_exempt
def getBaseInfo(request):
    return JsonResponse({
        'data': {
            'userInfo': {
                'basic': {
                    'username': 'SynHao'
                }
            },
        },
        'status': 200,
        'message': '请求成功',
    })


def getWorkspaceBaseInfo(request):
    return JsonResponse({
        "status": 0,
        "message": "OK",
        "data": {
            "roles": ["analyser", "developer"],
            "topUrl": "/home",
            "topName": "Scriptis",
            "workspaceId": 224
        }
    })


def getWorkspaces(request):
    return JsonResponse({
        'data': {
            'workspaces': [{
                'id': 9,
                'name': '瞧瞧',
                'description': '看看',
                'label': '这是,我的',
                'createTime': '2021-10-20 12:23:00'
            }],
        },
        'status': 200,
        'message': '请求成功'
    })


def getWorkspacesID(request):
    return JsonResponse({
        'data': {
            'workspace': {
                'id': 9,
                'name': '瞧瞧',
                'description': '看看',
                'label': '这是,我的',
                'createTime': '2021-10-20 12:23:00'
            },
        },
        'status': 200,
        'message': '请求成功'
    })


def getWorkspacesIDFavorites(request):
    return JsonResponse({
        'data': {
            'favorites': [{
                'id': 9,
                'name': '瞧瞧',
                'description': '看看',
                'label': '这是,我的',
                'createTime': '2021-10-20 12:23:00'
            }],
        },
        'status': 200,
        'message': '请求成功'
    })


def getWorkspacesIDManagements(request):
    return JsonResponse({
        'data': {
            'managements': [{
                'id': 9,
                'name': '瞧瞧',
                'description': '看看',
                'label': '这是,我的',
                'createTime': '2021-10-20 12:23:00'
            }],
        },
        'status': 200,
        'message': '请求成功'
    })


def getWorkspacesIDApplications(request):
    return JsonResponse({
        'data': {
            'applications': [{
                'id': 9,
                'name': '瞧瞧',
                'title': 'Title1',
                'description': '看看',
                'label': '这是,我的',
                'createTime': '2021-10-20 12:23:00'
            }, {
                'id': 10,
                'name': '瞧瞧1',
                'title': 'Title2',
                'description': '看看',
                'label': '这是,我的',
                'createTime': '2021-10-20 12:23:00'
            }],
        },
        'status': 200,
        'message': '请求成功'
    })


def getDepartments(request):
    return JsonResponse({
        'data': {
            'departments': [{
                'name': '瞧瞧',
                'description': '看看',
                'label': '这是,我的',
                'createTime': '2021-10-20 12:23:00'
            }],
        },
        'status': 200,
        'message': '请求成功'
    })


def getJobHistoryList(request):
    return JsonResponse({
        'data': {
            'tasks': ['dsdfs'],
        },
        'status': 200,
        'message': '请求成功'
    })


def getDemos(request):
    return JsonResponse({
        'data': {
            'demos': [{
                'title': '这是一个DEMO,workflow',
                'name': 'workflow'
            }, {
                'title': '这是一个DEMO,application',
                'name': 'application'
            }, {
                'title': '这是一个DEMO,visualization',
                'name': 'visualization'
            }, {
                'title': '这是一个DEMO,工作流',
                'name': '工作流'
            }, {
                'title': '这是一个DEMO,应用场景',
                'name': '应用场景'
            }, {
                'title': '这是一个DEMO,可视化',
                'name': '可视化'
            }],
        },
        'status': 200,
        'message': '请求成功'
    })


def getDatasourceAll(request):
    return JsonResponse({
        'data': {
            'departments': [{
                'name': '瞧瞧',
                'description': '看看',
                'label': '这是,我的',
                'createTime': '2021-10-20 12:23:00'
            }],
        },
        'status': 200,
        'message': '请求成功'
    })


def getUDFAll(request):
    return JsonResponse({
        "status": 0,
        "message": "OK",
        "data": {
            "udfTree": {
                "id": 121,
                "parent": 13,
                "name": 'fd',
                "userName": 'synhao',
                "description": 'synhao',
                "createTime": 1626768617000,
                "updateTime": 1626768617000,
                "category": '',
                "udfInfos": '',
                "childrens": [
                    {"id": 1,
                     "parent": -1,
                     "name": "系统函数",
                     "userName": "sys",
                     "description": "",
                     "createTime": 1626768617000,
                     "updateTime": 1626768617000,
                     "category": "udf",
                     "udfInfos": '',
                     "childrens": ''}
                ]
            }
        }
    })


def getUserRootPath(request):
    return JsonResponse({
        "method": "/api/filesystem/getUserRootPath",
        "status": 0,
        "message": "OK",
        "data": {
            "userLocalRootPath": "file:///data/linkis/dss_test01"
        }
    })


def getDirFileTrees(request):
    return JsonResponse({
        "method": "/api/filesystem/getDirFileTrees",
        "status": 0,
        "message": "OK",
        "data": {
            "dirFileTrees": {
                "name": "dss_test01",
                "path": "file:///data/linkis/dss_test01",
                "properties": None,
                "children": [
                    {
                        "name": "DEMO.py",
                        "path": "file:///data/linkis/dss_test01/DEMO.py",
                        "properties": {
                            "size": "155",
                            "modifytime": "1628086449000"
                        },
                        "children": None,
                        "isLeaf": None,
                        "parentPath": "file:///data/linkis/dss_test01"
                    },
                    {
                        "name": "DEMO.scala",
                        "path": "file:///data/linkis/dss_test01/DEMO.scala",
                        "properties": {
                            "size": "157",
                            "modifytime": "1628086449000"
                        },
                        "children": None,
                        "isLeaf": None,
                        "parentPath": "file:///data/linkis/dss_test01"
                    },
                    {
                        "name": "DEMO.python",
                        "path": "file:///data/linkis/dss_test01/DEMO.python",
                        "properties": {
                            "size": "363",
                            "modifytime": "1628086449000"
                        },
                        "children": None,
                        "isLeaf": True,
                        "parentPath": "file:///data/linkis/dss_test01"
                    },
                    {
                        "name": "DEMO.sql",
                        "path": "file:///data/linkis/dss_test01/DEMO.sql",
                        "properties": {
                            "size": "166",
                            "modifytime": "1628086449000"
                        },
                        "children": None,
                        "isLeaf": True,
                        "parentPath": "file:///data/linkis/dss_test01"
                    },
                    {
                        "name": "DEMO.hql",
                        "path": "file:///data/linkis/dss_test01/DEMO.hql",
                        "properties": {
                            "size": "166",
                            "modifytime": "1628086449000"
                        },
                        "children": None,
                        "isLeaf": True,
                        "parentPath": "file:///data/linkis/dss_test01"
                    },
                    {
                        "name": "DEMO.sh",
                        "path": "file:///data/linkis/dss_test01/DEMO.sh",
                        "properties": {
                            "size": "18",
                            "modifytime": "1628086449000"
                        },
                        "children": None,
                        "isLeaf": True,
                        "parentPath": "file:///data/linkis/dss_test01"
                    }
                ],
                "isLeaf": False,
                "parentPath": None
            }
        }
    })


def getVideos(request):
    return JsonResponse({
        'data': {
            'videos': [{
                'title': '这是一个DEMO,workflow',
                'name': 'workflow'
            }, {
                'title': '这是一个DEMO,application',
                'name': 'application'
            }, {
                'title': '这是一个DEMO,visualization',
                'name': 'visualization'
            }, {
                'title': '这是一个DEMO,工作流',
                'name': '工作流'
            }, {
                'title': '这是一个DEMO,应用场景',
                'name': '应用场景'
            }, {
                'title': '这是一个DEMO,可视化',
                'name': '可视化'
            }],
        },
        'status': 200,
        'message': '请求成功'
    })


def getDict(request, null=None):
    return JsonResponse({"code": 200, "message": "success", "data": {"data_type": [
        {"value": "1", "label": "维度", "type": null, "icon": null,
         "children": [{"value": "10000", "label": "字符串", "type": null, "icon": "1", "children": null},
                      {"value": "20000", "label": "数字", "type": null, "icon": "2", "children": null},
                      {"value": "30000", "label": "日期", "type": null, "icon": "3", "children": null}]},
        {"value": "2", "label": "指标", "type": null, "icon": null,
         "children": [{"value": "20001", "label": "整数", "type": null, "icon": "2", "children": null},
                      {"value": "20002", "label": "小数", "type": null, "icon": "2", "children": null},
                      {"value": "20003", "label": "货币", "type": null, "icon": "2", "children": null},
                      {"value": "20004", "label": "百分数", "type": null, "icon": "2", "children": null}]}],
        "dict_type": [{"key": "0", "value": "无"},
                      {"key": "1", "value": "枚举"},
                      {"key": "2", "value": "数据库"},
                      {"key": "3", "value": "函数"}],
        "cal_type": [{"key": "1", "value": "求和"},
                     {"key": "2", "value": "计数"}],
        "business_line": [{"key": "0", "value": "通用"},
                          {"key": "1", "value": "聚合"},
                          {"key": "2", "value": "SSP"},
                          {"key": "3", "value": "DSP"}],
        "database_column_type": {"10000": "String,varchar",
                                 "20000": "Int8,Int16,Int32,Int64,Float32,Float64,byte,short,int,bigint,long,float,double",
                                 "30000": "DateTime,timestamp,date"}}});


def getDMList(request, null=None):
    if request.method == 'POST':
        return JsonResponse({"code": 200, "message": "success", "data": [
            {"id": 62, "dsId": 1, "businessLine": 1, "tableName": "md_wide_model_distribute", "columnName": null,
             "tableNameShow": "聚合业务标准指标表(近一月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 63, "dsId": 1, "businessLine": 1, "tableName": "md_event_model_distribute", "columnName": null,
             "tableNameShow": "聚合业务标准事件表(近一月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 64, "dsId": 2, "businessLine": 1, "tableName": "md_pub_report_offline", "columnName": null,
             "tableNameShow": "聚合开发者离线报表", "columnNameShow": null, "dataType": null, "description": null, "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 67, "dsId": 2, "businessLine": 3, "tableName": "dsp_algo_delivery_inc_hour", "columnName": null,
             "tableNameShow": "DSP算法投放效果统计每小时增量表(近一周)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 71, "dsId": 5, "businessLine": 3, "tableName": "ads_dsp_bus_event_link_inc_day_distribute",
             "columnName": null, "tableNameShow": "DSP业务标准指标表(近一月)", "columnNameShow": null, "dataType": null,
             "description": null, "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 73, "dsId": 2, "businessLine": 3, "tableName": "dsp_adv_report_realtime", "columnName": null,
             "tableNameShow": "DSP广告源实时报表(近三月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 74, "dsId": 2, "businessLine": 3, "tableName": "dsp_funnel_report", "columnName": null,
             "tableNameShow": "DSP漏斗报表", "columnNameShow": null, "dataType": null, "description": null, "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 79, "dsId": 2, "businessLine": 3, "tableName": "dsp_rta_report_realtime", "columnName": null,
             "tableNameShow": "DSP RTA请求实时表", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 80, "dsId": 2, "businessLine": 3, "tableName": "dsp_rta_task_report_realtime", "columnName": null,
             "tableNameShow": "DSP RTA请求任务级实时表", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 105, "dsId": 2, "businessLine": 2, "tableName": "ssp_ad_report_realtime", "columnName": null,
             "tableNameShow": "SSP广告源实时报表(近三月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 107, "dsId": 2, "businessLine": 2, "tableName": "ssp_pub_report_realtime", "columnName": null,
             "tableNameShow": "SSP开发者实时报表(近三月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 110, "dsId": 1, "businessLine": 1, "tableName": "md_debug_info_distribute", "columnName": null,
             "tableNameShow": "聚合错误信息日志(近一周)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 111, "dsId": 1, "businessLine": 2, "tableName": "dws_ssp_bus_request_sd_inc_day", "columnName": null,
             "tableNameShow": "SSP业务线标准指标表(近一月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 112, "dsId": 1, "businessLine": 2, "tableName": "dws_ssp_bus_response_sd_inc_day",
             "columnName": null,
             "tableNameShow": "SSP业务线响应级指标表(近一月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 113, "dsId": 6, "businessLine": 1, "tableName": "account_log", "columnName": null,
             "tableNameShow": "天权用户访问数据表", "columnNameShow": null, "dataType": null, "description": null, "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 114, "dsId": 5, "businessLine": 3, "tableName": "dsp_bus_imp_mode_inc", "columnName": null,
             "tableNameShow": "DSP曝光模式表(近一月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 116, "dsId": 2, "businessLine": 2, "tableName": "ssp_real_traffic_report", "columnName": null,
             "tableNameShow": "SSP百青藤流量报表(近三月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 117, "dsId": 2, "businessLine": 3, "tableName": "dsp_bus_search_traffic_inc_day", "columnName": null,
             "tableNameShow": "DSP搜索广告流量分级表", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 118, "dsId": 5, "businessLine": 3, "tableName": "dsp_bus_search_detail_inc", "columnName": null,
             "tableNameShow": "DSP搜索词实时明细表(近一月)", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 119, "dsId": 2, "businessLine": 1, "tableName": "md_user_behavior_offline", "columnName": null,
             "tableNameShow": "聚合用户数据表", "columnNameShow": null, "dataType": null, "description": null, "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 120, "dsId": 2, "businessLine": 1, "tableName": "md_slot_user_behavior_offline", "columnName": null,
             "tableNameShow": "聚合广告位用户数据表", "columnNameShow": null, "dataType": null, "description": null, "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 121, "dsId": 1, "businessLine": 1, "tableName": "ads_md_bus_event_metric_inc_day",
             "columnName": null,
             "tableNameShow": "聚合2.0事件明细数据", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 122, "dsId": 1, "businessLine": 1, "tableName": "ads_md_bus_standard_metric_inc_day",
             "columnName": null,
             "tableNameShow": "聚合2.0标准指标数据", "columnNameShow": null, "dataType": null, "description": null,
             "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 124, "dsId": 1, "businessLine": 2, "tableName": "ssp_drop_traffic_report", "columnName": null,
             "tableNameShow": "SSP未填充流量表", "columnNameShow": null, "dataType": null, "description": null, "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 125, "dsId": 2, "businessLine": 1, "tableName": "finance_detailed_statement_of_income_and_cost",
             "columnName": null, "tableNameShow": "财务数据明细", "columnNameShow": null, "dataType": null,
             "description": null,
             "isTable": 1, "managePerm": 1, "updatePerm": null, "viewPerm": 1},
            {"id": 126, "dsId": 2, "businessLine": 1, "tableName": "finance_pm_view", "columnName": null,
             "tableNameShow": "账务运营数据明细", "columnNameShow": null, "dataType": null, "description": null, "isTable": 1,
             "managePerm": 1, "updatePerm": null, "viewPerm": 1}]})
    else:
        return null


def getMenuList(request, null=None):
    if request.method == 'POST':
        return JsonResponse({"code": 200, "message": "success", "data": [
            {"id": 4, "collectId": null, "isRoot": 1, "parentId": 0, "subType": 1, "icon": null, "menuType": 4,
             "menuName": "\\", "orderNum": 256.0, "ownerAccountId": 0, "modifiedOn": "2022-07-29T11:47:13.000+00:00",
             "managePerm": 1, "updatePerm": 1, "viewPerm": 1, "level": null, "menuList": null, "isPersonal": 0,
             "url": null, "childList": [
                {"id": 1000, "collectId": null, "isRoot": 0, "parentId": 4, "subType": 3, "icon": null, "menuType": 4,
                 "menuName": "Real Time", "orderNum": 128.0, "ownerAccountId": 100068,
                 "modifiedOn": "2022-08-02T02:04:14.000+00:00", "managePerm": 0, "updatePerm": 0, "viewPerm": 1,
                 "level": 1, "menuList": "4,", "isPersonal": 0,
                 "url": "https://davinci.ubixioe.com/share.html?shareToken=eNoNzbERADEIA8GWDAaMQ0BW_yX9ZxfszEHdLZULZ41ermI0hSM83h6l224ye08aUH1___K1zA1N566AqmAse2YCXH6QYxGrtExCtL3rFL1FHtirfcTm9cFst6r564kV5AD8l2G3SIWeD5GoJP0&type=dashboard#share/dashboard?Ubix_from=home",
                 "childList": []},
                {"id": 1001, "collectId": null, "isRoot": 0, "parentId": 4, "subType": 3, "icon": null, "menuType": 4,
                 "menuName": "Offline Matrix", "orderNum": 256.0, "ownerAccountId": 100068,
                 "modifiedOn": "2022-08-02T02:17:06.000+00:00", "managePerm": 0, "updatePerm": 0, "viewPerm": 1,
                 "level": 1, "menuList": "4,", "isPersonal": 0,
                 "url": "https://davinci.ubixioe.com/share.html?shareToken=eNoNzbkBwDAIBLCVzI_LA8z-IyWdOmHt1TklU3HFRAQIHa6mDEkFi97cLOnUGdQ105evqK9z2gp8mGlas7rbZ4_FZKv7AUPJicsKgbUierN1ypq0X8W0mAL965FiKGb2L10vdnk4PoVsJOE&type=dashboard#share/dashboard?Ubix_from=home",
                 "childList": []},
                {"id": 10011, "collectId": null, "isRoot": 0, "parentId": 4, "subType": 1, "icon": null, "menuType": 4,
                 "menuName": "MD Dashboard", "orderNum": 704.0, "ownerAccountId": 100068,
                 "modifiedOn": "2022-07-29T11:47:06.000+00:00", "managePerm": 1, "updatePerm": 0, "viewPerm": 0,
                 "level": 1, "menuList": "4,", "isPersonal": 0, "url": null, "childList": []},
                {"id": 10012, "collectId": null, "isRoot": 0, "parentId": 4, "subType": 1, "icon": null, "menuType": 4,
                 "menuName": "SSP Dashboard", "orderNum": 768.0, "ownerAccountId": 100068,
                 "modifiedOn": "2022-07-29T11:47:18.000+00:00", "managePerm": 1, "updatePerm": 0, "viewPerm": 0,
                 "level": 1, "menuList": "4,", "isPersonal": 0, "url": null, "childList": []},
                {"id": 10013, "collectId": null, "isRoot": 0, "parentId": 4, "subType": 1, "icon": null, "menuType": 4,
                 "menuName": "DSP Dashboard", "orderNum": 832.0, "ownerAccountId": 100068,
                 "modifiedOn": "2022-07-29T11:47:17.000+00:00", "managePerm": 1, "updatePerm": 0, "viewPerm": 1,
                 "level": 1, "menuList": "4,", "isPersonal": 0, "url": null, "childList": []},
                {"id": 10014, "collectId": null, "isRoot": 0, "parentId": 4, "subType": 1, "icon": null, "menuType": 4,
                 "menuName": "GD Dashboard", "orderNum": 896.0, "ownerAccountId": 100068,
                 "modifiedOn": "2022-07-29T11:47:18.000+00:00", "managePerm": null, "updatePerm": null,
                 "viewPerm": null, "level": 1, "menuList": "4,", "isPersonal": 0, "url": null, "childList": []},
                {"id": 10015, "collectId": null, "isRoot": 0, "parentId": 4, "subType": 1, "icon": null, "menuType": 4,
                 "menuName": "BDP Dashboard", "orderNum": 960.0, "ownerAccountId": 100068,
                 "modifiedOn": "2022-07-29T11:47:18.000+00:00", "managePerm": 1, "updatePerm": 0, "viewPerm": 0,
                 "level": 1, "menuList": "4,", "isPersonal": 0, "url": null, "childList": [
                    {"id": 10022, "collectId": null, "isRoot": 0, "parentId": 10015, "subType": 2, "icon": null,
                     "menuType": 4, "menuName": "用来画原型的报表", "orderNum": 1408.0, "ownerAccountId": 103,
                     "modifiedOn": "2022-07-29T11:47:14.000+00:00", "managePerm": 1, "updatePerm": 1, "viewPerm": 1,
                     "level": 2, "menuList": "4,10015,", "isPersonal": 0, "url": null, "childList": []},
                    {"id": 10237, "collectId": null, "isRoot": 0, "parentId": 10015, "subType": 2, "icon": null,
                     "menuType": 4, "menuName": "天权使用情况分析", "orderNum": 15168.0, "ownerAccountId": 103,
                     "modifiedOn": "2022-07-29T11:47:09.000+00:00", "managePerm": 1, "updatePerm": 1, "viewPerm": 1,
                     "level": 2, "menuList": "4,10015,", "isPersonal": 0, "url": null, "childList": []}]},
                {"id": 10548, "collectId": null, "isRoot": 0, "parentId": 4, "subType": 1, "icon": null, "menuType": 4,
                 "menuName": "财务", "orderNum": 1280.0, "ownerAccountId": 103,
                 "modifiedOn": "2022-08-01T04:29:46.000+00:00", "managePerm": 1, "updatePerm": 0, "viewPerm": 0,
                 "level": 1, "menuList": "4,", "isPersonal": 0, "url": null, "childList": []}]}]});
