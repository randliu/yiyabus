# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('seq', models.AutoField(serialize=False, primary_key=True)),
                ('pkg', models.FileField(upload_to=b'./pkgs', verbose_name=b'Package')),
                ('desc', models.TextField(default='\u66f4\u65b0\u63cf\u8ff0\uff1a')),
                ('timestamp', models.DateTimeField()),
                ('count', models.IntegerField(default=0)),
                ('qr', models.FileField(default=b'None', upload_to=b'./qr/', verbose_name=b'qr')),
            ],
        ),
    ]
