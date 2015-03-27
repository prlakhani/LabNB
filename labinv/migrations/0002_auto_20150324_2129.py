# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labinv', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tube',
            name='shortName',
        ),
        migrations.AddField(
            model_name='misctube',
            name='shortName',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='strip',
            name='shortName',
            field=models.CharField(max_length=50, default=''),
            preserve_default=False,
        ),
    ]
