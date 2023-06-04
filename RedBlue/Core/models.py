from django.core.validators import MinValueValidator
from django.db import models

from Account.models import Account


# Create your models here.

class Stavka(models.Model):
    owner_id = models.OneToOneField(Account, related_name="my_stavka", on_delete=models.CASCADE)
    color = models.CharField(max_length=1)
    quantity = models.IntegerField(validators=[MinValueValidator(25)])