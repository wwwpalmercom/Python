# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 05:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('Article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_comment', to='article.Article')),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
    ]
