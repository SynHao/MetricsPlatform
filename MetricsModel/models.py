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
