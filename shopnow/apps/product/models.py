from django.db import models
from shopnow.apps.profile.models import profile

class  category(models.Model):
    category =  models.CharField(max_length=50)
    description =  models.TextField()
    
    def __unicode__(self):
        category = "{0}".format(self.category)
        return category

class  subcategory(models.Model):
    id  =  models.IntegerField(primary_key=True)
    subcategory  = models.CharField(max_length=50)
    description  = models.TextField()
    
    def  __unicode__(self):
        subcategory = "{0}".format(self.subcategory)
        return subcategory

class product(models.Model):
    def imageproduct(self,filename):
        route = 'images/product/{0}/{1}'.format(self.title, filename)
        return route

    status           =       models.BooleanField()
    title            =       models.CharField(max_length=250)
    amount           =       models.IntegerField()
    state            =       models.CharField(max_length=100)
    price            =       models.DecimalField(max_digits=6, decimal_places=2)
    description      =       models.TextField(max_length=100000000)
    image1           =       models.ImageField(upload_to=imageproduct, null=True, blank=True)
    image2           =       models.ImageField(upload_to=imageproduct, null=True, blank=True)
    image3           =       models.ImageField(upload_to=imageproduct, null=True, blank=True)
    image4           =       models.ImageField(upload_to=imageproduct, null=True, blank=True)
    publicationday   =       models.DateField()
    expirationday    =       models.DateField()
    category         =       models.ManyToManyField(category)
    subcategory      =       models.ManyToManyField(subcategory)
    
    def __unicode__(self):
        title = "{0}".format(self.title)
        return title
