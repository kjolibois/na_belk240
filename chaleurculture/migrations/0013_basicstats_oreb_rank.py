# Generated by Django 2.1.7 on 2019-04-15 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaleurculture', '0012_auto_20190415_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicstats',
            name='OREB_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
