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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('shortName', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date(2015, 3, 23))),
                ('note', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='imgData',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('shortName', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date(2015, 3, 23))),
                ('note', models.TextField()),
                ('imgType', models.CharField(choices=[('gel', 'gel'), ('misc', 'misc')], max_length=10)),
                ('imgFile', models.ImageField(upload_to='images/<function imgData.get_imgType at 0x7f3d14bb5ea0>')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='gel',
            fields=[
                ('imgdata_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='data.imgData', auto_created=True)),
                ('key', models.TextField(verbose_name='Comma-separated by lane; semicolon separated for multiple rows')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.imgdata',),
        ),
        migrations.CreateModel(
            name='miscExp',
            fields=[
                ('experiment_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='data.Experiment', auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
        migrations.CreateModel(
            name='miscImg',
            fields=[
                ('imgdata_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='data.imgData', auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('data.imgdata',),
        ),
        migrations.CreateModel(
            name='survivalExp',
            fields=[
                ('experiment_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='data.Experiment', auto_created=True)),
                ('nInx', models.IntegerField(default=100, verbose_name='Number injected')),
                ('dailyDeathsExp', models.CommaSeparatedIntegerField(default='0,0,0,0,0,0,0,0', verbose_name='Experimental group deaths, comma separated', max_length=100)),
                ('expFinalSurviving', models.IntegerField(default=0, verbose_name='Experimental larvae surviving at 7 dpf')),
                ('nCtrl', models.IntegerField(default=300, verbose_name='Number of control embryos')),
                ('dailyDeathsCtrl', models.CommaSeparatedIntegerField(default='0,0,0,0,0,0,0,0', verbose_name='Control group deaths, comma separated', max_length=100)),
                ('ctrlFinalSurviving', models.IntegerField(default=0, verbose_name='Control larvae surviving at 7 dpf')),
                ('ctrlType', models.CharField(verbose_name='Control type: uninjected vs sham or cas9 injected, etc.', max_length=20)),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
        migrations.CreateModel(
            name='uInjection',
            fields=[
                ('experiment_ptr', models.OneToOneField(serialize=False, parent_link=True, primary_key=True, to='data.Experiment', auto_created=True)),
                ('gRNAvolume', models.DecimalField(max_digits=3, default=1.0, verbose_name='volume in uL', decimal_places=2)),
                ('cas9volume', models.DecimalField(max_digits=3, default=1.0, verbose_name='volume in uL', decimal_places=2)),
                ('totalVol', models.DecimalField(max_digits=3, decimal_places=2, verbose_name='total volume in uL')),
                ('injectVol', models.DecimalField(max_digits=2, decimal_places=1, verbose_name='injected volume in nL')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
    ]
