# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0010_auto_20150213_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='portfoliocard',
            options={'ordering': ['order'], 'verbose_name': 'Portfolio Card', 'verbose_name_plural': 'Portfolio Cards'},
        ),
    ]
