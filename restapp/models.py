from django.db import models

class Peoples(models.Model):
    name=models.CharField(max_length=100)
    # age=models.IntegerField(max_length=5)
    sex=models.CharField(max_length=4)
    country=models.CharField(max_length=50)



    def __str__(self):
        return self.name
    
