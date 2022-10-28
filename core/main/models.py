from django.db import models

# Create your models here.
class Car(models.Model):
    img = models.ImageField('Car image', upload_to='media')
    name = models.CharField('Car name', max_length=100)
    price = models.IntegerField('Car price')
    slug = models.SlugField('Slug name', unique=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'
        