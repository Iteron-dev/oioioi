# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-05-23 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0012_auto_20200128_1451'),
        ('scoresreveal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scorerevealconfig',
            name='problem_instance',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores_reveal_config', to='contests.ProblemInstance', verbose_name='problem instance'),
        ),
        migrations.AlterField(
            model_name='scorerevealconfig',
            name='problem',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='scores_reveal_config', to='problems.Problem', verbose_name='problem'),
        )
    ]