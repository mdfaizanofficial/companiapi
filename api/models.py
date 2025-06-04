from django.db import models
from django.db.models import ForeignKey, CASCADE


# Create your models here.

class Company(models.Model):
    company_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(
        ("IT", "IT"),
        ("Non-IT", "Non-IT")
    ))

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    position = models.CharField(max_length=100, choices=(
                                                        ('Manager', 'Manager'),
                                                        ('Software Developer', 'SD'),
                                                        ('Project Leader', 'PL')
                                                        )
    )

    company = models.ForeignKey(Company, on_delete=CASCADE)

    def __str__(self):
        return self.name
