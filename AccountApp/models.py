from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

class User(AbstractUser):
    pass
# Create your models here.
class Specialty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Doctor(User):
    phone_validator = RegexValidator(
        regex=r"^\d{8}$",
        message="Le téléphone doit contenir 8 chiffres."
    )

    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)]
    )

    phone = models.CharField(max_length=8, validators=[phone_validator])

    specialties = models.ManyToManyField(Specialty , related_name='doctors')

    def __str__(self):
        return self.get_full_name() or self.username

class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[
            RegexValidator(
                r"^\d{8}$",
                message="La CIN doit contenir 8 chiffres."
            )
        ]
    )

    phone = models.CharField(max_length=8)

    birth_date = models.DateField()

    def __str__(self):
        return self.get_full_name() or self.username