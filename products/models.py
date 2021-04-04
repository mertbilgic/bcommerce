from django.db import models
from django.db.models.base import Model

CATEGORY_CHOICES = (
    ('EL', 'Electronic'),
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    price = models.DecimalField(decimal_places=2, max_digits=25, blank=False)
    discount_price = models.DecimalField(decimal_places=2, max_digits=25, blank=True)
    image = models.ImageField()
    active = models.BooleanField(default=True)
    sold_out = models.BooleanField(default=False)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=1)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




