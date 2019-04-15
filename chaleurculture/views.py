from django.shortcuts import render
from chaleurculture.nbatesting import get_defense_stats,get_regular_stats,get_advanced_stats, parse_hustle_stats_page,get_roster_stats
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from chaleurculture.models import RosterStats,BasicStats,DefenseStats,AdvancedStats,HustleStats,UpdatesStats
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from chaleurculture.databasemiddleware import create_update_entry,create_advanced_entries,create_defense_entries,create_regular_entries,create_roster_entries,create_hustle_entries
from chaleurculture.serializers import UpdatesStatsSerializer
from datetime import datetime
# Create your views here.
@api_view(['GET', 'POST'])
def update_page(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        latest= UpdatesStats.objects.latest('insertionDate')
        serializer = UpdatesStatsSerializer(latest )

        return JsonResponse(serializer.data) #Response(serializer.data)
            
    elif request.method == 'POST':
        advanced_stats = get_advanced_stats()
        adstatus=create_advanced_entries(advanced_stats)
        

        defense_stats=get_defense_stats()
        dstatus=create_defense_entries(defense_stats)
        
        regular_stats=get_regular_stats()
        regstatus=create_regular_entries(regular_stats)
        
        hustle_stats=parse_hustle_stats_page('/home/khalil/django2019projects/nabelk240/chaleurculture/htmlhustle/NBA.com_Stats _ Players Hustle.html')
        hustatus=create_hustle_entries(hustle_stats)
        
        roster_stats=get_roster_stats()
        rostatus=create_roster_entries(roster_stats)
        update_stats={'HustleStatsStatus':hustatus, 
                'AdvancedStatsStatus':adstatus, 
                'RegStatsStatus':regstatus, 
                'DefenseStatsStatus':dstatus,
                'RosterStatsStatus':rostatus}
        create_update_entry(update_stats)
        serializer = UpdatesStatsSerializer(update_stats)

            #return "postworksinner"#Response(updateserializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data)#Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_test_page(request):
        if request.method == 'GET':
            #snippets = get_latest_update_status()
            advanced_stats=get_advanced_stats()
            #print(advanced_stats)
            create_advanced_entries(advanced_stats)
            defense_stats=get_defense_stats()
            create_defense_entries(defense_stats)
            #serializer = SnippetSerializer(snippets, many=True)
            return JsonResponse(advanced_stats,safe=False) #Response(serializer.data)
            '''
@api_view(['GET', 'POST'])
class MiamiHeatStats(ObjectMultipleModelAPIView):
    today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
    today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
    
    
    querylist = [
        {'queryset': RosterStats.objects.get(insertionDate_range=(today_min, today_max)), 'serializer_class': PlaySerializer},
        {'queryset': BasicStats.objects.get( insertionDate_range=(today_min, today_max)), 'serializer_class': PoemSerializer},
        {'queryset': DefenseStats.objects.get( insertionDate_range=(today_min, today_max)), 'serializer_class': PoemSerializer},
        {'queryset': AdvancedStats.objects.get( insertionDate_range=(today_min, today_max)), 'serializer_class': PoemSerializer},
        {'queryset': HustleStats.objects.get( insertionDate_range=(today_min, today_max)), 'serializer_class': PoemSerializer},
    ]
    '''