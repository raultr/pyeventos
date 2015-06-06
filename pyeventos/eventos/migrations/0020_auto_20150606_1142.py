# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0019_auto_20150606_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_evaluador',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 16, 42, 51, 930515, tzinfo=utc), verbose_name=b'fecha_evaluador'),
        ),
    ]
