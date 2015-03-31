# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20150331_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filedata',
            name='exp',
        ),
        migrations.AddField(
            model_name='gel',
            name='exp',
            field=models.ForeignKey(default=3, to='data.Experiment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='miscfile',
            name='exp',
            field=models.ForeignKey(default=3, to='data.Experiment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='miscimg',
            name='exp',
            field=models.ForeignKey(default=3, to='data.Experiment'),
            preserve_default=False,
        ),
    ]
