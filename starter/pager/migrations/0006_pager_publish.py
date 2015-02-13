# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0005_auto_20150213_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='pager',
            name='publish',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
