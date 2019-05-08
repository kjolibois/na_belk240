import requests
from .models import USAHomesRawData,USAHOMESaleInfo
import datetime
def get_homes_without_zip():
        url='http://localhost:5000/apirea/realestate/get25homes'    
        resp = requests.get(url=url)
        data = resp.json() #
        print(data[0])
        

        for element in data:
                USAHomesRawData.objects.create(
                entryID=element['id'],
                emaildate=element['emailDate'],            
                insertionDate = datetime.datetime.now(),
                date_modified = None,
                zipcode = None,
                address= element['address'],
                state = element['state'],
                city= element['city'],
                homeid=element['id'],   
                        )
                #USAHomesRawData.save()
        return data
     
def update_homes_without_zip():
    print("updating")

def update_sales_price():
    print("salesprice")

def sales_info():
    print("pricehistory")



