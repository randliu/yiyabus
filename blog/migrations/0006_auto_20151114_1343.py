# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogspost_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogspost',
            name='version',
        ),
        migrations.AddField(
            model_name='demo',
            name='version',
            field=models.CharField(default=b'2.2.0', max_length=30),
        ),
    ]
