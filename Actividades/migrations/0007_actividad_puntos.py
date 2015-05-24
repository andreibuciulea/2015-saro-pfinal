# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0006_usuario_rss'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='puntos',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
