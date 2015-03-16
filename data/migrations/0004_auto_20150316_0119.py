# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20150316_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgdata',
            name='imgFile',
            field=models.ImageField(upload_to='images/<function imgData.get_imgType at 0x7f150f276b70>'),
            preserve_default=True,
        ),
    ]
