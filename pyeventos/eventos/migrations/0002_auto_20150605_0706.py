# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='cdu_fuente',
            field=models.ForeignKey(related_name='evento_cdu_fuente', default=b'0030000', to='catalogos_detalle.CatalogoDetalle'),
        ),
    ]
