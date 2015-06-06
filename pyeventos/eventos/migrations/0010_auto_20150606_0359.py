# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0009_auto_20150606_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_capturista',
            field=models.DateTimeField(default=b'1900-01-01 00:00:00', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_evaluador',
            field=models.DateTimeField(default=b'1900-01-01 00:00:00', blank=True),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_filtro',
            field=models.DateTimeField(default=b'1900-01-01 00:00:00', blank=True),
        ),
    ]
