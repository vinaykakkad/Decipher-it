# Generated by Django 3.1 on 2021-02-01 07:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=220, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('fullname', models.CharField(blank=True, max_length=220, null=True)),
                ('current_round', models.IntegerField(default=0)),
                ('current_que', models.IntegerField(default=1)),
                ('points', models.IntegerField(default=-3)),
                ('last_ans_time', models.TimeField(default=datetime.datetime(2020, 8, 27, 16, 0))),
                ('last_round_time', models.TimeField(default=datetime.datetime(2020, 8, 27, 16, 0))),
                ('is_disqualified', models.BooleanField(default=False)),
                ('is_countdown_active', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_activated', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]