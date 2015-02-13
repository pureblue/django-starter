# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0013_auto_20150213_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagerSocial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=50)),
                ('service_url', models.URLField()),
            ],
            options={
                'verbose_name': 'Social Service',
                'verbose_name_plural': 'Social Services',
            },
            bases=(models.Model,),
        ),
    ]
