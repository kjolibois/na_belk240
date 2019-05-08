from django.shortcuts import render
from rest_framework.decorators import api_view
from zillna.apicalls import get_homes_without_zip
from rest_framework.response import Response
from zillna.models import USAHomesRawData
from zillna.zillowtesting import get_zillow_info
from zillna.zipcodetesting import get_zip_code, gmap_call
# Create your views here.
@api_view(['GET', 'POST'])
def update_zip(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        latest= get_homes_without_zip()
        #serializer = UpdatesStatsSerializer(latest )
        return Response(latest)
        #return JsonResponse(serializer.data) #Response(serializer.data)
    '''        
    elif request.method == 'POST':
       
       

            #return ""#Response(updateserializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data)#Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
@api_view(['GET', 'POST'])
def get_zip(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        get_zip_code()
        twentyFiveHomes=  USAHomesRawData.objects.exclude(zipcode__isnull=True).values()
        #serializer = UpdatesStatsSerializer(latest )
        return Response(twentyFiveHomes)
        #return JsonResponse(serializer.data) #Response(serializer.data)
    '''        
    elif request.method == 'POST':
       
       

            #return ""#Response(updateserializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data)#Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

@api_view(['GET', 'POST'])
def get_price(request):
    """
    List all code snippets, or create a new snippet.
    """

    if request.method == 'GET':
        prices=get_zillow_info(30)
        #serializer = UpdatesStatsSerializer(latest )
        return Response(prices)
        #return JsonResponse(serializer.data) #Response(serializer.data)
    '''        
    elif request.method == 'POST':
       
       

            #return ""#Response(updateserializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.data)#Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''