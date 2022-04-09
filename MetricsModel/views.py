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


def get_meta_info(type=MetaInfoModel.MetaType):
    """
    获取元数据信息
    :arg type 元数据类型
    """
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

# return JsonResponse({"data":
#     {"list":
#         [{
#             "id": "fake-list-0",
#             "owner": "付小小",
#             "title": "Alipay",
#             "avatar": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
#             "cover": "https://gw.alipayobjects.com/zos/rmsportal/uMfMFlvUuceEyPpotzlq.png",
#             "status": "active",
#             "percent": 68,
#             "logo": "https://gw.alipayobjects.com/zos/rmsportal/WdGqmHpayyMjiEhcKoVE.png",
#             "href": "https://ant.design",
#             "updatedAt": 1636956540072,
#             "createdAt": 1636956540072,
#             "subDescription": "那是一种内在的东西， 他们到达不了，也无法触及的",
#             "description": "在中台产品的研发过程中，会出现不同的设计规范和实现方式，但其中往往存在很多类似的页面和组件，这些类似的组件会被抽离成一套标准规范。",
#             "activeUser": 132840,
#             "newUser": 1823,
#             "star": 159,
#             "like": 142,
#             "message": 15,
#             "content": "段落示意：蚂蚁金服设计平台 "
#                        "ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。蚂蚁金服设计平台 "
#                        "ant.design，用最小的工作量，无缝接入蚂蚁金服生态，提供跨越设计与开发的体验解决方案。",
#             "members": [{
#                 "avatar": "https://gw.alipayobjects.com/zos/rmsportal/ZiESqWwCXBRQoaPONSJe"
#                           ".png",
#                 "name": "曲丽丽",
#                 "id": "member1"
#             }]
#         }
#         ]}
# })
