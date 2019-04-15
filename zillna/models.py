from django.db import models

# Create your models here.
class USAHOMESaleInfo(models.Model):
    """This class represents the info after zillow model."""
    entryID = models.CharField(max_length=255, blank=False, unique=True)
    insertionDate = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    zipcode = models.CharField(max_length=255, blank=False, unique=False)
    address= models.CharField(max_length=255, blank=False, unique=True)
    sales_price=  models.DecimalField(max_digits=20, decimal_places=5, default=None)
    state =models.CharField(max_length=255, blank=False, unique=False)
    city= models.CharField(max_length=255, blank=False, unique=False)
    homeid= models.CharField(max_length=255, blank=False, unique=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

class USAHomesRawData(models.Model):
    """This class represents the homesinfo scraped from email and pulled from aspnet api model."""
    entryID = models.CharField(max_length=255, blank=False, unique=True)
    insertionDate = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    zipcode = models.CharField(max_length=255, blank=False, unique=False)
    address= models.CharField(max_length=255, blank=False, unique=True)
    state =models.CharField(max_length=255, blank=False, unique=False)
    city= models.CharField(max_length=255, blank=False, unique=False)
    homeid= models.CharField(max_length=255, blank=False, unique=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)   
class USAHomesPriceHistory(models.Model):
    """This class represents the homesinfo scraped from email and pulled from aspnet api model."""
    price= models.CharField(max_length=255, blank=False, unique=True)
    insertionDate = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date= models.CharField(max_length=255, blank=False, unique=False)
    homeid= models.CharField(max_length=255, blank=False, unique=False)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)   
       