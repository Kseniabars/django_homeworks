import slugify
from django.db import models


class Phone(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places = 2, default = 0.00)
    image = models.ImageField(upload_to = 'templates/')
    release_date = models.DateField()
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name
