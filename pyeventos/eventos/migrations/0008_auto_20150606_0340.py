# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0007_auto_20150606_0337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_evaluador',
            field=models.DateField(default=b'1900-01-01'),
        ),
    ]
