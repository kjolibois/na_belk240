from .models import USAHomesRawData,USAHOMESaleInfo

def get_zip_code():
    #get 200 entries that are zipcode null
    with open("~/home/khalil/gmaps_key.conf", 'r') as f:
        key = f.readline().replace("\n", "")
    twentyFiveHomes= USAHOMESaleInfo.objects.get()
    for home in twentyFiveHomes:
    #make into a function for iteration
        zip= gmap_call(home.address,key)
        home.zipcode = zip
        home.save()
        print('YEAH')

def gmap_call(address,key):
    from googlemaps import GoogleMaps

    gmaps = GoogleMaps(key)
    address = address
    result = gmaps.geocode(address)
    placemark = result['Placemark'][0]
    details = placemark['AddressDetails']['Country']['AdministrativeArea']
    street = details['Locality']['Thoroughfare']['ThoroughfareName']
    city = details['Locality']['LocalityName']
    state = details['AdministrativeAreaName']
    zipcode = details['Locality']['PostalCode']['PostalCodeNumber']
    print( ', '.join((street, city, state, zipcode)))

    return zipcode