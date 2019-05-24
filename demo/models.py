from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator
    )
from django.db import models
from django.urls import reverse

from .managers import UserManager


NAME_REGEX = '^[a-zA-Z ]*$'
EMAIL_REGEX= '^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$'

GENDER_CHOICE = (
    ("Male", "Male"),
    ("Female", "Female"),
    )


class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    full_name = models.CharField(
        max_length=256,
        blank=False,
        validators=[
                RegexValidator(
                    regex=NAME_REGEX,
                    message='Name must be Alphabetic',
                    code='invalid_full_name'
                    )
                ]
        )

    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(
        unique=True, blank=False,
        validators=[
                RegexValidator(
                    regex=EMAIL_REGEX,
                    message='please_enter_valid_email',
                    code='invalid_Email_id'
                    )
                ]
        )
    contact_no = models.IntegerField(unique=True)
    Address = models.CharField(max_length=512)
    nationality = models.CharField(max_length=256)
    occupation = models.CharField(max_length=256)
    picture = models.ImageField(
        null=True,
        blank=True,
        height_field="height_field",
        width_field="width_field",
        )

    height_field = models.IntegerField(default=600, null=True)
    width_field = models.IntegerField(default=600, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'  # use email to log in
    REQUIRED_FIELDS = []  # required when user is created

    def __str__(self):
        return str(self.id)
