# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('logo_text', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('caption', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Pager',
                'verbose_name_plural': 'Pagers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PagerBackgroundImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=b'background_image')),
            ],
            options={
                'verbose_name': 'Background Image',
                'verbose_name_plural': 'Background Images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PagerBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_slug', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('in_nav', models.BooleanField(default=True)),
                ('order', models.IntegerField(default=b'0')),
                ('pager_background_image', models.ForeignKey(blank=True, to='pager.PagerBackgroundImage', null=True)),
            ],
            options={
                'ordering': ['-order'],
                'verbose_name': 'Pager Block',
                'verbose_name_plural': 'Page Blocks',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PortfolioCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_slug', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('order', models.IntegerField(default=b'0')),
            ],
            options={
                'ordering': ['-order'],
                'verbose_name': 'Portfolio Card',
                'verbose_name_plural': 'Portfolio Cards',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PortfolioImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=b'portfolio_image')),
            ],
            options={
                'verbose_name': 'Portfolio Image',
                'verbose_name_plural': 'Portfolio Images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StaffCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('title_slug', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('order', models.IntegerField(default=b'0')),
            ],
            options={
                'ordering': ['-order'],
                'verbose_name': 'Staff Card',
                'verbose_name_plural': 'Staff Cards',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StaffImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=b'staff_image')),
            ],
            options={
                'verbose_name': 'Staff Image',
                'verbose_name_plural': 'Staff Images',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='staffcard',
            name='staff_image',
            field=models.ForeignKey(blank=True, to='pager.StaffImage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='portfoliocard',
            name='portfolio_image',
            field=models.ForeignKey(blank=True, to='pager.PortfolioImage', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagerblock',
            name='portfolio_cards',
            field=models.ManyToManyField(help_text=b'If this is a portfolio section, what portfolio cards do you want to include?', to='pager.PortfolioCard', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pagerblock',
            name='staff_cards',
            field=models.ManyToManyField(help_text=b'If this is a staff section, what staff cards do you want to include?', to='pager.StaffCard', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='pager',
            name='pager_blocks',
            field=models.ManyToManyField(to='pager.PagerBlock'),
            preserve_default=True,
        ),
    ]
