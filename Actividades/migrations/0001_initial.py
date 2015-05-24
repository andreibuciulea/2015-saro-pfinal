# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('precio', models.CharField(max_length=100)),
                ('fecha', models.CharField(max_length=100)),
                ('hora', models.CharField(max_length=32)),
                ('duracion', models.CharField(max_length=100)),
                ('larga_duracion', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
                ('seleccionado', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=32)),
                ('pagina', models.ManyToManyField(to='Actividades.Actividad')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
