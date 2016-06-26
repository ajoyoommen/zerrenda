# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 15:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(editable=False, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.List'),
        ),
    ]