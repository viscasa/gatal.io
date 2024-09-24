from django.db import models
from django.contrib.auth.models import User
import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    price = models.IntegerField()
    description = models.TextField()
    genre = models.TextField()

    # @property
    # def is_mood_strong(self):
    #     return self.mood_intensity > 5