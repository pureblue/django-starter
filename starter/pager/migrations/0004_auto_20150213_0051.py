# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0003_auto_20150213_0044'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagerblock',
            old_name='title_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='portfoliocard',
            old_name='title_slug',
            new_name='slug',
        ),
        migrations.RenameField(
            model_name='staffcard',
            old_name='title_slug',
            new_name='slug',
        ),
    ]
