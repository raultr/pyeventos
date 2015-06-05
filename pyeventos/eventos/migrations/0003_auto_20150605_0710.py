# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_auto_20150605_0706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='cdu_estado',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='cdu_municipio',
        ),
    ]
