# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150324_1615'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gel',
            old_name='imgFile',
            new_name='gelFile',
        ),
        migrations.RenameField(
            model_name='miscfile',
            old_name='file',
            new_name='userFile',
        ),
        migrations.RemoveField(
            model_name='inxsurvivalexp',
            name='ctrlFinalSurviving',
        ),
        migrations.RemoveField(
            model_name='inxsurvivalexp',
            name='expFinalSurviving',
        ),
        migrations.RemoveField(
            model_name='survivalexp',
            name='expFinalSurviving',
        ),
        migrations.AlterField(
            model_name='gel',
            name='key',
            field=models.TextField(verbose_name='Key; comma-separated by lane; semicolon separated for multiple rows'),
            preserve_default=True,
        ),
    ]
