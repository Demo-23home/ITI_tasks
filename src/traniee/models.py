from django.db import models

# Create your models here.



class Traniee(models.Model):

    usrnme = models.CharField(max_length=20)
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=60)
    track = models.CharField(max_length=20)
    passwd= models.CharField(max_length=8)


    def __str__(self):
        return self.f_name