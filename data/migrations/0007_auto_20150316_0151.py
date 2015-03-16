# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20150316_0124'),
    ]

    operations = [
        migrations.CreateModel(
            name='miscExp',
            fields=[
                ('experiment_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='data.Experiment', auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
        migrations.CreateModel(
            name='miscImg',
            fields=[
                ('imgdata_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='data.imgData', auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('data.imgdata',),
        ),
        migrations.AlterField(
            model_name='imgdata',
            name='imgFile',
            field=models.ImageField(upload_to='images/<function imgData.get_imgType at 0x7f71f944e048>'),
            preserve_default=True,
        ),
    ]
