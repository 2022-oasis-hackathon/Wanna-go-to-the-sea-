from django.db import models

# Create your models here.
class house(models.Model):
    name = models.CharField(max_length=20)
    content = models.CharField(max_length=40)
    price = models.CharField(max_length=20)
    reputation = models.FloatField(max_length=20)

	#uploadedFile = models.FileField(upload_to="")
