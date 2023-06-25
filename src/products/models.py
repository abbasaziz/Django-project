from django.db import models

# Create your models here.


class Product(models.Model):
    # maxlength is always required as an attribute
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(blank=True)
    featured = models.BooleanField(default=True)
    # This is usually set to null=True of default=True. But since previously migrated models do not have this object, we will run it as is, and set the it as true in the CLI which will then prompt Django to make all these changes in the previously migrated or saved models in the DB as well.
