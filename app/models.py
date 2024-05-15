from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Farmer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Land(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Size in acres
    description = models.TextField()

    def __str__(self):
        return f'{self.location} ({self.size} acres)'



    
class Lease(models.Model):
    land = models.ForeignKey('Land', on_delete=models.CASCADE)
    lessee = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    farmer_approved = models.BooleanField(default=False)
    lessee_approved = models.BooleanField(default=False)