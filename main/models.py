from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    # time = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField()
    genre = models.TextField()

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5