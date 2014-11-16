# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('score', models.IntegerField()),
                ('submitter', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('hn_id', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
