# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 19:15
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('micro', '0011_auto_20161217_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default=b'settings.MEDIA_ROOT/media/a.jpg', storage=django.core.files.storage.FileSystemStorage(location=b'/Users/sareenzhang/Desktop/ls/art-c-master/web/scalica/media'), upload_to=b'media'),
        ),
    ]