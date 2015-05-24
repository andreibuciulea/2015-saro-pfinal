# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0004_actividad_id_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='fondo',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
    ]
