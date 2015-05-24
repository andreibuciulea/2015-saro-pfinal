# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0003_usuario_titulo_p'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='id_evento',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
