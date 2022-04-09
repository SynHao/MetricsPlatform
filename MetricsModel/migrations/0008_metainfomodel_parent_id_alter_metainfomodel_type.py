# Generated by Django 4.0.3 on 2022-04-09 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetricsModel', '0007_alter_metainfomodel_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='metainfomodel',
            name='parent_id',
            field=models.BigIntegerField(default=0, verbose_name='父级ID'),
        ),
        migrations.AlterField(
            model_name='metainfomodel',
            name='type',
            field=models.IntegerField(choices=[(1, 'Business'), (2, 'Metrics'), (3, 'Time Cycle')], verbose_name='元数据类型.1:业务线;2:指标词根'),
        ),
    ]