# Generated by Django 4.0.3 on 2022-04-09 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MetricsModel', '0004_alter_metainfomodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metainfomodel',
            name='type',
            field=models.IntegerField(choices=[(1, 'Business')], verbose_name='元数据类型.1:业务线;'),
        ),
    ]
