# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-14 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_date', models.DateField()),
                ('leave_type', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='leave',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LeavePortal.Resource'),
        ),
    ]
