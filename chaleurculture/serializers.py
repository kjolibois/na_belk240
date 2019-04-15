from rest_framework import serializers
from chaleurculture.models import RosterStats,BasicStats,DefenseStats,AdvancedStats,HustleStats,UpdatesStats

class UpdatesStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UpdatesStats
        fields =  ('insertionDate',
                    'date_modified',
                    'HustleStatsStatus',
                    'AdvancedStatsStatus',
                    'RegStatsStatus',
                    'DefenseStatsStatus',
                    'RosterStatsStatus')


class Rosterserializer(serializers.ModelSerializer):
    class Meta:
        model = RosterStats
        fields =  ('insertionDate',
                    'date_modified',
                    'HustleStatsStatus',
                    'AdvancedStatsStatus',
                    'RegStatsStatus',
                    'DefenseStatsStatus',
                    'RosterStatsStatus')

class Advancedserializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedStats
        fields =  ('insertionDate',
                    'date_modified',
                    'HustleStatsStatus',
                    'AdvancedStatsStatus',
                    'RegStatsStatus',
                    'DefenseStatsStatus',
                    'RosterStatsStatus')
class Regularserializer(serializers.ModelSerializer):
    class Meta:
        model = BasicStats
        fields =  ('insertionDate',
                    'date_modified',
                    'HustleStatsStatus',
                    'AdvancedStatsStatus',
                    'RegStatsStatus',
                    'DefenseStatsStatus',
                    'RosterStatsStatus')
class DefenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefenseStats
        fields =  ('insertionDate',
                    'date_modified',
                    'HustleStatsStatus',
                    'AdvancedStatsStatus',
                    'RegStatsStatus',
                    'DefenseStatsStatus',
                    'RosterStatsStatus')


class HustleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HustleStats
        fields =  ('insertionDate',
                    'date_modified',
                    'HustleStatsStatus',
                    'AdvancedStatsStatus',
                    'RegStatsStatus',
                    'DefenseStatsStatus',
                    'RosterStatsStatus')