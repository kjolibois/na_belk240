# Generated by Django 2.1.7 on 2019-04-15 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaleurculture', '0013_basicstats_oreb_rank'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicstats',
            name='CFID',
            field=models.CharField(default=None, max_length=255),
        ),
        migrations.AddField(
            model_name='basicstats',
            name='CFPARAMS',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
