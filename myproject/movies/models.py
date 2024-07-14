from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)  # Corrected field name
    release_year = models.IntegerField()
    genre = models.CharField(max_length=50)
    director = models.CharField(max_length=100)
    rating = models.FloatField()
    
    def __str__(self):
        return self.title
