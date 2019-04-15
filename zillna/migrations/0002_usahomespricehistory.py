# Generated by Django 2.1.7 on 2019-04-14 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zillna', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USAHomesPriceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=255, unique=True)),
                ('insertionDate', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date', models.CharField(max_length=255)),
                ('homeid', models.CharField(max_length=255)),
            ],
        ),
    ]
