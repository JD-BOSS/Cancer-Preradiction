from django.db import models

#Gender	Age	Smoking	Fatigue	Allergy	Cancer


# Create your models here.
class Cancer(models.Model):
    Gender=models.FloatField(max_length=20)
    Age=models.FloatField(max_length=20)
    Smoking=models.FloatField(max_length=20)
    Fatigue=models.FloatField(max_length=20)
    Allergy=models.FloatField(max_length=20)