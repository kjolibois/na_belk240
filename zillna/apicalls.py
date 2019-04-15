import requests
from .models import USAHomesRawData,USAHOMESaleInfo
import datetime
def getHomeswithoutzip():
    url='http://localhost:5000/apirea/realestate/get25homes'    
    resp = requests.get(url=url)
    data = resp.json() #
    print(data[0])
    for element in data:
        USAHomesRawData.objects.create(
                        
            insertionDate = datetime.datetime.now(),
            date_modified = None,
            zipcode = None,
            address= element.address ,
            state = element.state,
            city= element.city,
            homeid=element.id,   
                     )
        USAHomesRawData.save()

def updateHomeswithoutzip():
    print("updating")

def updatesalesprice():
    print("salesprice")

def salesinfo():
    print("pricehistory")




getHomeswithoutzip()