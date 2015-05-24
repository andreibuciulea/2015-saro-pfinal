# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0005_usuario_fondo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rss',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
