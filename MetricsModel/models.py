from django.db import models


class FileSystemListModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    path = models.CharField(max_length=255)
    size = models.IntegerField()
    create_by = models.CharField(max_length=150)
    create_time = models.DateTimeField(auto_created=True)
    modify_by = models.CharField(max_length=150)
    modify_time = models.DateTimeField(auto_now=True)


class MetricList(models.Model):
    class BusinessType(models.IntegerChoices):
        SSP = 1

    id = models.BigAutoField(primary_key=True)
    metric_key = models.CharField(max_length=30)
    metric_name = models.CharField(max_length=30)
    metric_desc = models.CharField(max_length=255, blank=True)
    metric_topic = models.CharField(max_length=255, blank=True)
    business_type = models.IntegerField(choices=BusinessType.choices, blank=True)
    metric_filed = models.CharField(max_length=30, blank=True)
    time_cycle = models.CharField(max_length=30, blank=True)
    metric_dim = models.JSONField(default=None, blank=True)
    metric_alias = models.CharField(max_length=30, blank=True)
    metric_owner = models.IntegerField(default=0, blank=True)
    metric_level = models.IntegerField(default=0, blank=True)
    metric_power = models.JSONField(blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    create_user = models.IntegerField(default=0)
    update_time = models.DateTimeField(auto_now=True)
    update_user = models.IntegerField(default=0)


class MetaInfoModel(models.Model):
    """词根信息（元信息）管理模型"""

    class MetaType(models.IntegerChoices):
        """MetaType定义元数据的类型"""
        business = 1
        metrics = 2
        time_cycle = 3
        dim = 4
        dim_value = 5

    id = models.BigAutoField(primary_key=True, verbose_name="自增键")
    type = models.IntegerField(choices=MetaType.choices, verbose_name="元数据类型.1:业务线;2:指标词根")
    value = models.CharField(max_length=30, verbose_name="元数据英文KEY")
    label = models.CharField(max_length=30, verbose_name="元数据中文值", default=None)
    parent_id = models.BigIntegerField("父级ID", default=0);
    create_by = models.CharField(max_length=150, verbose_name="创建人")
    create_time = models.DateTimeField('创建时间', auto_created=True)
    modify_by = models.CharField(max_length=150, verbose_name="更新人")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
