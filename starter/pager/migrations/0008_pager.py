# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pager', '0007_delete_pager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(help_text=b'The name by which the template author retrieves this content.', unique=True, max_length=255)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Pager content',
            },
            bases=(models.Model,),
        ),
    ]
