# Generated by Django 4.0.3 on 2022-04-09 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetricsModel', '0006_alter_metainfomodel_options_remove_metainfomodel_key_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metainfomodel',
            name='type',
            field=models.IntegerField(choices=[(1, 'Business'), (2, 'Metrics')], verbose_name='元数据类型.1:业务线;2:指标词根'),
        ),
    ]
