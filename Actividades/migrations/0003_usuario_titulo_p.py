# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0002_usuario_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='titulo_p',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
