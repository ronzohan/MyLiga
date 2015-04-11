# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myliga', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='name',
            new_name='email',
        ),
        migrations.AddField(
            model_name='manager',
            name='address',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manager',
            name='contact_no',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manager',
            name='first_name',
            field=models.CharField(max_length=50, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='manager',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2015, 4, 11, 15, 7, 15, 904105, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
    ]
