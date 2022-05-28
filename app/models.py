from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# Create your models here.
class Cred(models.Model):

    username = models.CharField(max_length=256)
    password = models.CharField(max_length=512)
    website = models.CharField(max_length=128)
    category_id = models.ForeignKey(Category, default=2, on_delete=models.DO_NOTHING)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.website
