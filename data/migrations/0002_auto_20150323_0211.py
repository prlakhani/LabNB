# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
        ('contenttypes', '0001_initial'),
        ('labinv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uinjection',
            name='cas9',
            field=models.ForeignKey(to='labinv.cas9', related_name='cas9'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='uinjection',
            name='gRNA',
            field=models.ForeignKey(to='labinv.gRNA', related_name='gRNA'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='uinjection',
            name='otherTubes',
            field=models.ManyToManyField(blank=True, null=True, to='labinv.Tube'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='survivalexp',
            name='inx',
            field=models.ForeignKey(to='data.uInjection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imgdata',
            name='exp',
            field=models.ForeignKey(to='data.Experiment'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='imgdata',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, to='contenttypes.ContentType', related_name='polymorphic_data.imgdata_set'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='gel',
            name='tubes',
            field=models.ManyToManyField(blank=True, null=True, to='labinv.Tube'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='experiment',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, to='contenttypes.ContentType', related_name='polymorphic_data.experiment_set'),
            preserve_default=True,
        ),
    ]
