# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0006_pager_publish'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pager',
        ),
    ]
