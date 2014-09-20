from django.db import models
from django.contrib.auth.models import User

class profile(models.Model):
    def avatarroute(self,filename):
        route = 'Avatar/Users/{0}/{1}'.format(self.user,filename)
        return route

    CHOICES=[('mujer','mujer'),('hombre','hombre')]

    user =  models.OneToOneField(User, unique=True)
    avatar =  models.ImageField(upload_to=avatarroute)
    phone =  models.CharField(max_length=13)
    cellphone =  models.CharField(max_length=13)
    address = models.CharField(max_length=300)
    sex =  models.CharField(choices=CHOICES,max_length=6)
    dateofbirth = models.DateField()
    occupation = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    
    def  __unicode__(self):
        return  self.user.username
