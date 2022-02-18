from rest_framework import serializers


class MetricListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    metric_key = serializers.CharField(max_length=30, required=True)
    metric_name = serializers.CharField(max_length=30)
    metric_desc = serializers.CharField(max_length=255)
    metric_topic = serializers.CharField(max_length=255)
    business_type = serializers.IntegerField()
    metric_filed = serializers.CharField(max_length=30)
    time_cycle = serializers.CharField(max_length=30)
    metric_dim = serializers.JSONField(default=None)
    metric_alias = serializers.CharField(max_length=30)
    metric_owner = serializers.IntegerField(default=0)
    metric_level = serializers.IntegerField(default=0)
    metric_power = serializers.JSONField()
    create_time = serializers.DateTimeField()
    create_user = serializers.IntegerField(default=0)
    update_time = serializers.DateTimeField()
    update_user = serializers.IntegerField(default=0)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
