from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField(max_length=250)
    price = models.FloatField()
    series = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', kwargs={'game_id': self.id})