# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='qr',
            field=models.URLField(default=b'qq.com'),
        ),
    ]
