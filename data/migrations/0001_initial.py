# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date(2015, 3, 16))),
                ('note', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='survivalExp',
            fields=[
                ('experiment_ptr', models.OneToOneField(auto_created=True, serialize=False, to='data.Experiment', parent_link=True, primary_key=True)),
                ('initPop', models.IntegerField(verbose_name='Initial population')),
                ('dailyDeathsExp', models.CommaSeparatedIntegerField(max_length=100, verbose_name='Experimental group deaths, comma separated')),
                ('dailyDeathsCtrl', models.CommaSeparatedIntegerField(max_length=100, verbose_name='Control group deaths, comma separated')),
                ('ctrlType', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
        migrations.CreateModel(
            name='uInjection',
            fields=[
                ('experiment_ptr', models.OneToOneField(auto_created=True, serialize=False, to='data.Experiment', parent_link=True, primary_key=True)),
                ('gRNAvolume', models.DecimalField(max_digits=3, decimal_places=2, default=1.0, verbose_name='volume in uL')),
                ('cas9volume', models.DecimalField(max_digits=3, decimal_places=2, default=1.0, verbose_name='volume in uL')),
                ('totalVol', models.DecimalField(max_digits=3, decimal_places=2, verbose_name='total volume in uL')),
                ('injectVol', models.DecimalField(max_digits=2, decimal_places=1, verbose_name='injected volume in nL')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
    ]
