# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151114_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demo',
            name='qr',
            field=models.URLField(default='\u4e0d\u8981\u7f16\u8f91\u6211'),
        ),
    ]
