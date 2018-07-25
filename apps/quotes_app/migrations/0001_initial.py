# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=1000)),
                ('favorites', models.ManyToManyField(related_name='faves', to='logreg_app.User')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='logreg_app.User')),
            ],
        ),
    ]
