from django.db import models


class Fruit(models.Model):
    name = models.CharField(max_length=120, null=True)
    description = models.TextField(blank=True, null=False)
    price = models.FloatField(null=True)
    date_create = models.DateField(auto_now_add=True)
    date_expired = models.DateField(null=False)
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=False)
    exist = models.BooleanField(default=True, null=True)


# ID (Django автоматически создаст)
# name
# description
# price
# date_create
# date_expired
# photo
# exist (Логическое удаление)