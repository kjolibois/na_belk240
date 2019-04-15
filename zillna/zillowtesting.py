import pprint
import zillow
from .models import USAHomesRawData,USAHOMESaleInfo
import datetime
api = zillow.ValuationApi()
def get_zillow_info(n):
    with open("/bin/config/zillow_key.conf", 'r') as f:
        key = f.readline().replace("\n", "")
   
   
    nentries = USAHomesRawData.objects.get().all()[:n]

    #get n entries from db where zipcode not null
    for home in nentries:
        #iterate through and post results 
        address = "3400 Pacific Ave., Marina Del Rey, CA"
        #postal_code = "90292"
        data = api.GetSearchResults(key, address)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(data.get_dict())
        #get sales history sales and asking price
        USAHOMESaleInfo.objects.create(
            salesprice= data.salesprice,
            insertionDate = datetime.datetime.now(),
            date_modified = None,
            zipcode =home.zipcode,
            address= home.address ,
            state = home.state,
            city= home.city,
            homeid=home.id,   
                     )
        USAHOMESaleInfo.save()


def get_price_history_info(n):
    with open("/bin/config/zillow_key.conf", 'r') as f:
        key = f.readline().replace("\n", "")
    nentries = USAHOMESaleInfo.objects.get().all()[:n]
    #get n entries from db where zipcode not null
    for home in nentries:
        #iterate through and post results 
        address = "3400 Pacific Ave., Marina Del Rey, CA"
        #postal_code = "90292"
        data = api.GetSearchResults(key, address)
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint(data.get_dict())
        #get sales history sales and asking price

