# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-13 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDetails',
            fields=[
                ('menuid', models.AutoField(primary_key=True, serialize=False)),
                ('menu_name', models.CharField(max_length=200)),
                ('menu_description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'menu_details',
            },
        ),
    ]
