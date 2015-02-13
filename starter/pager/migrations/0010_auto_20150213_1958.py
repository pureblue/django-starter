# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0009_pagerblock_background_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliocard',
            name='client',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='portfoliocard',
            name='client_website',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='portfoliocard',
            name='project_date',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='portfoliocard',
            name='service',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pagerblock',
            name='background_color',
            field=models.CharField(max_length=6, blank=True),
            preserve_default=True,
        ),
    ]
