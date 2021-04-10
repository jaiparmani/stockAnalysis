from django.db import models

# Create your models here.

class User(models.Model):

    email = models.EmailField()
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)



class FavStock(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=50)

    #https://api.twelvedata.com/stocks?exchange=BSE&source=docs
    




