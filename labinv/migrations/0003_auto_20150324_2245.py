# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labinv', '0002_auto_20150324_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='grna',
            name='primerF',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grna',
            name='primerR',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grna',
            name='prodSize',
            field=models.IntegerField(default=300, verbose_name='PCR product size for these primers'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='strip',
            name='key',
            field=models.TextField(verbose_name='Key; comma-separated by tube; semicolon if >1 in set'),
            preserve_default=True,
        ),
    ]
