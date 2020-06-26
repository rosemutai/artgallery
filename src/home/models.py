from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ArtCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'ArtCategories'
class Art(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(ArtCategory, on_delete=models.CASCADE)
    artist = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Art'

    def __str__(self):
        return self.title
    

