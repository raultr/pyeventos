# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0012_auto_20150606_0405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='observaciones',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
