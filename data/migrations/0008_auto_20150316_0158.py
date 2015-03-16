# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20150316_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgdata',
            name='imgFile',
            field=models.ImageField(upload_to='images/<function imgData.get_imgType at 0x7fd83b5fc048>'),
            preserve_default=True,
        ),
    ]
