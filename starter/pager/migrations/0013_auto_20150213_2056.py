# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0012_auto_20150213_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagerblock',
            name='font_color',
            field=models.CharField(max_length=6, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagerblock',
            name='text_align',
            field=models.CharField(max_length=6, blank=True),
            preserve_default=True,
        ),
    ]
