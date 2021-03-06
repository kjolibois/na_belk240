# Generated by Django 2.1.7 on 2019-04-15 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaleurculture', '0009_remove_advancedstats_entryid'),
    ]

    operations = [
        migrations.AddField(
            model_name='defensestats',
            name='AGE',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='BLK',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='BLK_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='CFID',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='CFPARAMS',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='DEF_RATING',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='DEF_RATING_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='DEF_WS',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='DEF_WS_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='DREB',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='DREB_PCT',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='DREB_PCT_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='DREB_RANK',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='GP',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='GP_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='L',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='L_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='MIN',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='MIN_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='OPP_PTS_2ND_CHANCE',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='OPP_PTS_2ND_CHANCE_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='OPP_PTS_FB',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='OPP_PTS_FB_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='OPP_PTS_OFF_TOV',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='OPP_PTS_OFF_TOV_RANK',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defensestats',
            name='OPP_PTS_PAINT',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='OPP_PTS_PAINT_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='PCT_BLK',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='PCT_BLK_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='PCT_DREB',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='PCT_DREB_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='PCT_STL',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='PCT_STL_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='PLAYER_ID',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defensestats',
            name='STL',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='STL_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='TEAM_ID',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='defensestats',
            name='W',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='W_PCT',
            field=models.DecimalField(decimal_places=5, default=None, max_digits=20),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='W_PCT_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='defensestats',
            name='W_RANK',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
