from rest_framework import serializers
from chaleurculture.models import RosterStats,BasicStats,DefenseStats,AdvancedStats,HustleStats,UpdatesStats
from django.contrib.auth.models import User

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


class RosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RosterStats
        fields =  '__all__'

class AdvancedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvancedStats
        fields = '__all__'
  
  
class RegularSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicStats
        fields = '__all__'
      
       

class DefenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = DefenseStats
        fields = '__all__'


class HustleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HustleStats
        fields = '__all__'



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username' )