# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0022_auto_20150606_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='prioridad',
            field=models.DecimalField(default=1.0, max_digits=5, decimal_places=2),
        ),
    ]
