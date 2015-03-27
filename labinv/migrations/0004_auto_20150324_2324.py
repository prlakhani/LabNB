# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labinv', '0003_auto_20150324_2245'),
    ]

    operations = [
        migrations.AddField(
            model_name='misctube',
            name='sequence',
            field=models.CharField(verbose_name='Sequence, if applicable (primers)', max_length=200, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grna',
            name='primerF',
            field=models.ForeignKey(related_name='primerF', blank=True, to='labinv.miscTube', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grna',
            name='primerR',
            field=models.ForeignKey(related_name='primerR', blank=True, to='labinv.miscTube', null=True),
            preserve_default=True,
        ),
    ]
