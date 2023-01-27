from django.db import models

# Create your models here.
class User(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  username = models.CharField(
    max_length=1000,
    null=False,
    blank=False
  )

  password = models.CharField(
    max_length=1000,
    null=False,
    blank=False
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  last_updated = models.DateTimeField(
    auto_now=True,
    null=False,
    blank=False
  )
