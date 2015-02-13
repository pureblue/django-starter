# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0004_auto_20150213_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pager',
            name='pager_blocks',
        ),
        migrations.AlterField(
            model_name='staffcard',
            name='phone',
            field=models.CharField(max_length=15, blank=True),
            preserve_default=True,
        ),
    ]
