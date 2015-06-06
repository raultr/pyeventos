# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0015_auto_20150606_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='fecha_evaluador',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 6, 16, 31, 16, 526109, tzinfo=utc), verbose_name=b'fecha_evaluador'),
        ),
    ]