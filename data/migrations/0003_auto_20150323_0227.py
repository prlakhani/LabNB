# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20150323_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imgdata',
            name='imgFile',
            field=models.ImageField(upload_to='images/<function imgData.get_imgType at 0x7fd94a294ea0>'),
            preserve_default=True,
        ),
    ]
