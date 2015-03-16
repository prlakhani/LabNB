# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tube',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date(2015, 3, 16))),
                ('exists', models.BooleanField(default=True)),
                ('note', models.TextField()),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='strip',
            fields=[
                ('tube_ptr', models.OneToOneField(auto_created=True, serialize=False, to='labinv.Tube', parent_link=True, primary_key=True)),
                ('key', models.TextField(verbose_name='Comma-separated by tube; semicolon if >1 in set')),
            ],
            options={
                'abstract': False,
            },
            bases=('labinv.tube',),
        ),
        migrations.CreateModel(
            name='gRNA',
            fields=[
                ('tube_ptr', models.OneToOneField(auto_created=True, serialize=False, to='labinv.Tube', parent_link=True, primary_key=True)),
                ('geneTarget', models.CharField(max_length=10)),
                ('targetSeq', models.CharField(max_length=30)),
                ('promoter', models.CharField(max_length=10, choices=[('T7', 'T7'), ('SP6', 'SP6')])),
                ('concentration', models.FloatField(verbose_name='concentration in ng/uL')),
            ],
            options={
                'abstract': False,
            },
            bases=('labinv.tube',),
        ),
        migrations.CreateModel(
            name='cas9',
            fields=[
                ('tube_ptr', models.OneToOneField(auto_created=True, serialize=False, to='labinv.Tube', parent_link=True, primary_key=True)),
                ('c9type', models.CharField(max_length=10, choices=[('mRNA', 'mRNA'), ('protein', 'protein')])),
                ('concentration', models.FloatField(verbose_name='concentration in ng/uL')),
            ],
            options={
                'abstract': False,
            },
            bases=('labinv.tube',),
        ),
        migrations.AddField(
            model_name='tube',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_labinv.tube_set', null=True, editable=False, to='contenttypes.ContentType'),
            preserve_default=True,
        ),
    ]