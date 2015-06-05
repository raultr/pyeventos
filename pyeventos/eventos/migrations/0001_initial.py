# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('catalogos_detalle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descripcion', models.CharField(max_length=1000)),
                ('criticidad_capturista', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('criticidad_evaluador', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('reporta', models.CharField(max_length=100)),
                ('observaciones', models.CharField(max_length=1000)),
                ('fecha_capturista', models.DateField(default=b'1900-01-01')),
                ('fecha_filtro', models.DateField(default=b'1900-01-01')),
                ('fecha_evaluador', models.DateField(default=b'1900-01-01')),
                ('revisada', models.BooleanField(default=False)),
                ('cdu_estado', models.ForeignKey(related_name='evento_cdu_estado', default=b'0010000', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_fuente', models.ForeignKey(related_name='evento_cdu_fuente', default=b'', to='catalogos_detalle.CatalogoDetalle')),
                ('cdu_municipio', models.ForeignKey(related_name='evento_cdu_municipio', default=b'0020000', to='catalogos_detalle.CatalogoDetalle')),
            ],
        ),
    ]
