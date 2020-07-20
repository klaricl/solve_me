from django.db import models

# Create your models here.
class Profile(models.Model):
    is_add = models.BooleanField(default = False)
    is_sub = models.BooleanField(default = False)
    is_mul = models.BooleanField(default = False)
    is_div = models.BooleanField(default = False)
    is_mul_range = models.BooleanField(default = False)
    is_mul_max_result = models.BooleanField(default = False)
    add_min = models.IntegerField(default = 0)
    add_max = models.IntegerField(default = 100)
    sub_min = models.IntegerField(default = 0)
    sub_max = models.IntegerField(default = 100)
    mul_min = models.IntegerField(default = 0)
    mul_max = models.IntegerField(default = 10)
    mul_result_max = models.IntegerField(default = 100)
    div_result_max = models.IntegerField(default = 100)
    with_negative_result = models.BooleanField(default = False)
    more_than_one_mul_or_div = models.BooleanField(default = False)
