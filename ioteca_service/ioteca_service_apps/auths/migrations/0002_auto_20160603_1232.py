# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-03 12:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auths', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='module',
            field=models.CharField(choices=[(b'WEB', b'Web informativa'), (b'ADMISION', b'Admisi\xc3\xb3n'), (b'BACKEND', b'Backend Manager'), (b'OTHER', 'Other')], default=b'BACKEND', max_length=50, verbose_name='module'),
        ),
    ]
