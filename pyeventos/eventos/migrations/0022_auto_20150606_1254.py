# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0021_auto_20150606_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_capturista',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'fecha_capturista'),
        ),
        migrations.AlterField(
            model_name='evento',
            name='fecha_filtro',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'fecha_filtro'),
        ),
    ]
