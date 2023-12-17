from django.db import models

# Create your models here.
class Restraunt(models.Model):
    username =  models.CharField(max_length=255)
    restruant_name = models.CharField(max_length=255)
    Address = models.CharField(max_length=255)
    
    # to give name to profile object representation

class SearchHistory (models.Model):
    search_date = models.CharField(max_length=255)
    restaurant_name = models.CharField(max_length=255)