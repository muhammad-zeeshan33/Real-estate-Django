from django.db.models.deletion import DO_NOTHING
from pages import admin
from django.db import models
from agents.models import Agent
from datetime import datetime

class Listing(models.Model):
    agent = models.ForeignKey(Agent, on_delete=DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    description = models.TextField(blank= True)
    price = models.IntegerField()
    area = models.CharField(max_length=20)
    beds = models.IntegerField()
    baths = models.IntegerField()
    Garage = models.IntegerField(default=0)
    is_sold = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    photo_main = models.ImageField(upload_to='photos/%y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True )
    photo_2 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True )
    photo_3 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True )
    photo_4 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True )
    photo_5 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True )
    photo_6 = models.ImageField(upload_to='photos/%y/%m/%d/', blank=True )
    list_date = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return self.title