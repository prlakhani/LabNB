# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labinv', '0002_auto_20150316_0119'),
    ]

    operations = [
        migrations.CreateModel(
            name='miscTube',
            fields=[
                ('tube_ptr', models.OneToOneField(primary_key=True, parent_link=True, to='labinv.Tube', auto_created=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            bases=('labinv.tube',),
        ),
    ]
