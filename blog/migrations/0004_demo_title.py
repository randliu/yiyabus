# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151114_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='title',
            field=models.CharField(default=b'new show', max_length=100),
        ),
    ]
