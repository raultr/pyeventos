# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0001_initial'),
        ('eventos', '0003_auto_20150605_0710'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='criticidad_capturista',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='criticidad_evaluador',
        ),
        migrations.AddField(
            model_name='evento',
            name='cdu_estado',
            field=models.ForeignKey(related_name='evento_cdu_estado', default=b'0010000', to='catalogos_detalle.CatalogoDetalle'),
        ),
        migrations.AddField(
            model_name='evento',
            name='cdu_municipio',
            field=models.ForeignKey(related_name='evento_cdu_municipio', default=b'0020000', to='catalogos_detalle.CatalogoDetalle'),
        ),
    ]
