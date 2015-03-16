# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        ('labinv', '0001_initial'),
        ('data', '0002_auto_20150316_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='imgData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortName', models.CharField(max_length=50)),
                ('date', models.DateField(default=datetime.date(2015, 3, 16))),
                ('note', models.TextField()),
                ('imgType', models.CharField(max_length=10, choices=[('gel', 'gel'), ('misc', 'misc')])),
                ('imgFile', models.ImageField(upload_to='images/<function imgData.get_imgType at 0x7fbf0f785b70>')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='gel',
            fields=[
                ('imgdata_ptr', models.OneToOneField(primary_key=True, to='data.imgData', parent_link=True, auto_created=True, serialize=False)),
                ('key', models.TextField(verbose_name='Comma-separated by lane; semicolon separated for multiple rows')),
                ('tubes', models.ManyToManyField(null=True, blank=True, to='labinv.Tube')),
            ],
            options={
                'abstract': False,
            },
            bases=('data.imgdata',),
        ),
        migrations.AddField(
            model_name='imgdata',
            name='polymorphic_ctype',
            field=models.ForeignKey(null=True, editable=False, related_name='polymorphic_data.imgdata_set', to='contenttypes.ContentType'),
            preserve_default=True,
        ),
    ]
