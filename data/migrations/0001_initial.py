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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=50)),
                ('date', models.DateField(verbose_name='Date; if in doubt, end date', default=datetime.date(2015, 3, 24))),
                ('note', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='fileData',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date(2015, 3, 24))),
                ('note', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='gel',
            fields=[
                ('filedata_ptr', models.OneToOneField(primary_key=True, to='data.fileData', serialize=False, parent_link=True, auto_created=True)),
                ('key', models.TextField(verbose_name='Comma-separated by lane; semicolon separated for multiple rows')),
                ('imgFile', models.ImageField(upload_to='images/gels/')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.filedata',),
        ),
        migrations.CreateModel(
            name='inxSurvivalExp',
            fields=[
                ('experiment_ptr', models.OneToOneField(primary_key=True, to='data.Experiment', serialize=False, parent_link=True, auto_created=True)),
                ('nInx', models.IntegerField(verbose_name='Number injected', default=100)),
                ('dailyDeathsExp', models.CommaSeparatedIntegerField(max_length=100, verbose_name='Experimental group deaths, comma separated', default='0,0,0,0,0,0,0,0')),
                ('expFinalSurviving', models.IntegerField(verbose_name='Experimental larvae surviving at 7 dpf', default=0)),
                ('nCtrl', models.IntegerField(verbose_name='Number of control embryos', default=300)),
                ('dailyDeathsCtrl', models.CommaSeparatedIntegerField(max_length=100, verbose_name='Control group deaths, comma separated', default='0,0,0,0,0,0,0,0')),
                ('ctrlFinalSurviving', models.IntegerField(verbose_name='Control larvae surviving at 7 dpf', default=0)),
                ('ctrlType', models.CharField(max_length=20, verbose_name='Control type: uninjected vs sham or cas9 injected, etc.')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
        migrations.CreateModel(
            name='miscExp',
            fields=[
                ('experiment_ptr', models.OneToOneField(primary_key=True, to='data.Experiment', serialize=False, parent_link=True, auto_created=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
        migrations.CreateModel(
            name='miscFile',
            fields=[
                ('filedata_ptr', models.OneToOneField(primary_key=True, to='data.fileData', serialize=False, parent_link=True, auto_created=True)),
                ('file', models.FileField(upload_to='files/')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.filedata',),
        ),
        migrations.CreateModel(
            name='miscImg',
            fields=[
                ('filedata_ptr', models.OneToOneField(primary_key=True, to='data.fileData', serialize=False, parent_link=True, auto_created=True)),
                ('imgFile', models.ImageField(upload_to='images/misc/')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.filedata',),
        ),
        migrations.CreateModel(
            name='survivalExp',
            fields=[
                ('experiment_ptr', models.OneToOneField(primary_key=True, to='data.Experiment', serialize=False, parent_link=True, auto_created=True)),
                ('nExp', models.IntegerField(verbose_name='Number injected', default=100)),
                ('dailyDeathsExp', models.CommaSeparatedIntegerField(max_length=100, verbose_name='Experimental group deaths, comma separated', default='0,0,0,0,0,0,0,0')),
                ('expFinalSurviving', models.IntegerField(verbose_name='Experimental larvae surviving at 7 dpf', default=0)),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
        migrations.CreateModel(
            name='uInjection',
            fields=[
                ('experiment_ptr', models.OneToOneField(primary_key=True, to='data.Experiment', serialize=False, parent_link=True, auto_created=True)),
                ('gRNAvolume', models.DecimalField(max_digits=3, verbose_name='volume in uL', default=1.0, decimal_places=2)),
                ('cas9volume', models.DecimalField(max_digits=3, verbose_name='volume in uL', default=1.0, decimal_places=2)),
                ('totalVol', models.DecimalField(max_digits=3, verbose_name='total volume in uL', decimal_places=2)),
                ('injectVol', models.DecimalField(max_digits=2, verbose_name='injected volume in nL', decimal_places=1)),
                ('strain', models.CharField(max_length=20, verbose_name='which strain of fish were injected')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.experiment',),
        ),
    ]
