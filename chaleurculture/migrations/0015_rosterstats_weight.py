# Generated by Django 2.1.7 on 2019-04-15 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaleurculture', '0014_auto_20190415_1300'),
    ]

    operations = [
        migrations.AddField(
            model_name='rosterstats',
            name='WEIGHT',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
