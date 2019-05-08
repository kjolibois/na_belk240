import pprint
import zillow
from .models import USAHomesRawData,USAHOMESaleInfo
import datetime
from zillna.customerrors import DontOverloadZillowError
api = zillow.ValuationApi()
def get_zillow_info(n):
    try:
        with open("zillna/zillow_key.conf", 'r') as f:
            key = f.readline().replace("\n", "")
        print(key)
        if(n>500):
            raise DontOverloadZillowError("Very bad mistake.", "too many calls: limit is 1000 a day try not to get near it ")

    

        nentries = USAHomesRawData.objects.exclude(zipcode__isnull=True)[:n]
        
        #get n entries from db where zipcode not null
        for home in nentries:
            try:
                #iterate through and post results 
                address = home.address
                postal_code = home.zipcode
                data = api.GetDeepSearchResults(key, address,postal_code)
                pp = pprint.PrettyPrinter(indent=4)
                data=data.get_dict()
                #get sales history sales and asking price
                if(data['extended_data']['last_sold_date']!=None):
                    USAHOMESaleInfo.objects.create(
                        sales_price= data['extended_data']['last_sold_price'],
                        insertionDate = datetime.datetime.now(),
                        date_modified = None,
                        zipcode =home.zipcode,
                        address= home.address ,
                        state = home.state,
                        city= home.city,
                        sales_date=data['extended_data']['last_sold_date'],
                        usecode=  data['extended_data']['usecode'],
                        year_built= data['extended_data']['year_built'],
                        bathrooms=data['extended_data']['bathrooms'],
                        bedrooms=data['extended_data']['bedrooms'],
                        tax_assessment=data['extended_data']['tax_assessment'],
                        tax_assessment_year=data['extended_data']['tax_assessment_year'],
                        latitude=data['full_address']['latitude'],
                        longitude=data['full_address']['longitude'],
                                )
            except zillow.ZillowError:
                print("zillow error")
                continue #add logging or return   
            
  
        return data
    except DontOverloadZillowError as error:
        print(str(error))
        return "Detail: {}".format(error.errors)
    


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

