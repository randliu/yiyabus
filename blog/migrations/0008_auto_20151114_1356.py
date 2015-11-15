# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20151114_1345'),
    ]

    operations = [
        migrations.CreateModel(
            name='QRUrl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField(default=b'qq.com')),
            ],
        ),
        migrations.RemoveField(
            model_name='demo',
            name='qr',
        ),
        migrations.AddField(
            model_name='qrurl',
            name='demo',
            field=models.ForeignKey(to='blog.Demo'),
        ),
    ]
