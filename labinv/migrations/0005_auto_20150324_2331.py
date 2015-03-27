# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labinv', '0004_auto_20150324_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grna',
            name='primerF',
            field=models.OneToOneField(blank=True, related_name='primerF', null=True, to='labinv.miscTube'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='grna',
            name='primerR',
            field=models.OneToOneField(blank=True, related_name='primerR', null=True, to='labinv.miscTube'),
            preserve_default=True,
        ),
    ]
