# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151114_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qrurl',
            name='demo',
            field=models.OneToOneField(to='blog.Demo'),
        ),
    ]
