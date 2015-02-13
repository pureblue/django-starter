# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0011_auto_20150213_2032'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pagerblock',
            options={'ordering': ['order'], 'verbose_name': 'Pager Block', 'verbose_name_plural': 'Page Blocks'},
        ),
        migrations.AlterModelOptions(
            name='staffcard',
            options={'ordering': ['order'], 'verbose_name': 'Staff Card', 'verbose_name_plural': 'Staff Cards'},
        ),
    ]
