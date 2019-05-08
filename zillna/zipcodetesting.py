from .models import USAHomesRawData,USAHOMESaleInfo
from googlemaps import googlemaps
from geopy.geocoders import Nominatim
def get_zip_code():
    #get 200 entries that are zipcode null
    with open("zillna/gmaps_key.conf", 'r') as f:
        key = f.readline().replace("\n", "")
    print(key)
    twentyFiveHomes=  USAHomesRawData.objects.all()
    for home in twentyFiveHomes:
    #make into a function for iteration
        print(home.address)
        zip= gmap_call(home.address,key)
        print(zip)
        home.zipcode = zip
        home.save()
        #print('YEAH')
        '''
def gmap_call(address,key):
    geolocator = Nominatim(user_agent="nabelk")
    location = geolocator.geocode(address)
    print(location)
'''
def gmap_call(address,key):

    gmaps = googlemaps.Client(key=key)
    address = address
    result = gmaps.geocode(address)
    
  
    for item in result[0]['address_components']:
        if item["types"][0] == 'postal_code':
        
            zipcode=item['short_name']
            return zipcode
    #print( ', '.join((street, city, state, zipcode)))

    
