# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Actividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='url',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
    ]
