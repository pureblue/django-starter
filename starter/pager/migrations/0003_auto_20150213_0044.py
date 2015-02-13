# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0002_auto_20150212_2349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffcard',
            old_name='title',
            new_name='staff_first_name',
        ),
        migrations.RenameField(
            model_name='staffcard',
            old_name='content',
            new_name='staff_short_bio',
        ),
        migrations.AddField(
            model_name='staffcard',
            name='email',
            field=models.EmailField(max_length=75, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='staffcard',
            name='phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='staffcard',
            name='staff_last_name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
