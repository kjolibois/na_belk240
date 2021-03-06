# Generated by Django 2.1.7 on 2019-04-14 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chaleurculture', '0007_auto_20190414_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdvancedStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entryID', models.CharField(max_length=255, unique=True)),
                ('insertionDate', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('PLAYER_ID', models.CharField(default=None, max_length=255)),
                ('PLAYER_NAME', models.CharField(default=None, max_length=255)),
                ('TEAM_ID', models.CharField(default=None, max_length=255)),
                ('GP', models.CharField(default=None, max_length=255)),
                ('W', models.CharField(default=None, max_length=255)),
                ('L', models.CharField(default=None, max_length=255)),
                ('W_PCT', models.CharField(default=None, max_length=255)),
                ('MIN', models.CharField(default=None, max_length=255)),
                ('eOFF_RATING', models.CharField(default=None, max_length=255)),
                ('OFF_RATING', models.CharField(default=None, max_length=255)),
                ('sp_work_OFF_RATING', models.CharField(default=None, max_length=1000)),
                ('eDEF_RATING', models.CharField(default=None, max_length=255)),
                ('DEF_RATING', models.CharField(default=None, max_length=255)),
                ('sp_work_DEF_RATING', models.CharField(default=None, max_length=255)),
                ('eNET_RATING', models.CharField(default=None, max_length=255)),
                ('NET_RATING', models.CharField(default=None, max_length=255)),
                ('sp_work_NET_RATING', models.CharField(default=None, max_length=255)),
                ('AST_PCT', models.CharField(default=None, max_length=255)),
                ('AST_TO', models.CharField(default=None, max_length=255)),
                ('AST_RATIO', models.CharField(default=None, max_length=255)),
                ('OREB_PCT', models.CharField(default=None, max_length=255)),
                ('DREB_PCT', models.CharField(default=None, max_length=255)),
                ('REB_PCT', models.CharField(default=None, max_length=255)),
                ('EFG_PCT', models.CharField(default=None, max_length=255)),
                ('TS_PCT', models.CharField(default=None, max_length=255)),
                ('USG_PCT', models.CharField(default=None, max_length=255)),
                ('ePACE', models.CharField(default=None, max_length=255)),
                ('PACE', models.CharField(default=None, max_length=255)),
                ('sp_work_PACE', models.CharField(default=None, max_length=255)),
                ('PIE', models.CharField(default=None, max_length=255)),
                ('FGM', models.CharField(default=None, max_length=255)),
                ('FGA', models.CharField(default=None, max_length=255)),
                ('FGM_PG', models.CharField(default=None, max_length=255)),
                ('FGA_PG', models.CharField(default=None, max_length=255)),
                ('FG_PCT', models.CharField(default=None, max_length=255)),
                ('GP_RANK', models.CharField(default=None, max_length=255)),
                ('W_RANK', models.CharField(default=None, max_length=255)),
                ('L_RANK', models.CharField(default=None, max_length=255)),
                ('W_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('MIN_RANK', models.CharField(default=None, max_length=255)),
                ('eOFF_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('OFF_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('sp_work_OFF_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('eDEF_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('DEF_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('sp_work_DEF_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('eNET_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('NET_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('sp_work_NET_RATING_RANK', models.CharField(default=None, max_length=255)),
                ('AST_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('AST_TO_RANK', models.CharField(default=None, max_length=255)),
                ('AST_RATIO_RANK', models.CharField(default=None, max_length=255)),
                ('OREB_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('DREB_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('REB_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('TM_TOV_PCT', models.CharField(default=None, max_length=255)),
                ('TM_TOV_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('EFG_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('TS_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('USG_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('ePACE_RANK', models.CharField(default=None, max_length=255)),
                ('PACE_RANK', models.CharField(default=None, max_length=255)),
                ('sp_work_PACE_RANK', models.CharField(default=None, max_length=255)),
                ('PIE_RANK', models.CharField(default=None, max_length=255)),
                ('FGM_RANK', models.CharField(default=None, max_length=255)),
                ('FGA_RANK', models.CharField(default=None, max_length=255)),
                ('FGM_PG_RANK', models.CharField(default=None, max_length=255)),
                ('FGA_PG_RANK', models.CharField(default=None, max_length=255)),
                ('FG_PCT_RANK', models.CharField(default=None, max_length=255)),
                ('CFID', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='Advanced_Stats',
        ),
    ]
