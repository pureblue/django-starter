# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0008_pager'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagerblock',
            name='background_color',
            field=models.CharField(default=1, max_length=6),
            preserve_default=False,
        ),
    ]
