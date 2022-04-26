from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

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

class Review(models.Model):
    date = models.DateField()
    review = models.TextField(max_length=250)
    rating = models.IntegerField(default=5, validators=[MaxValueValidator(5),MinValueValidator(1)])
    game = models.ForeignKey(Game, on_delete=models.CASCADE) # game_id
    def __str__(self):
        return f"{self.review}: {self.rating}, {self.date}"
    
    class Meta:
        ordering = ['-date']

