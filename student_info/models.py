from django.db import models



# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    mobile_number = models.IntegerField(blank=True,null=True)
    email = models.EmailField(max_length=254)
    location = models.CharField(max_length=250)
    technical_skills = models.CharField(max_length=250)

    def __str__(self):
        return self.name