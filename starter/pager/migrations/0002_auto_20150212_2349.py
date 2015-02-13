# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagerbackgroundimage',
            name='name',
            field=models.CharField(default=1, help_text=b'Name your image', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='portfolioimage',
            name='name',
            field=models.CharField(default=1, help_text=b'Name your image', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staffimage',
            name='name',
            field=models.CharField(default=1, help_text=b'Name your image', max_length=100),
            preserve_default=False,
        ),
    ]
