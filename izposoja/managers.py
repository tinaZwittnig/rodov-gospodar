from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
class UserManager(BaseUserManager):
    def create_user(self, email, telefonska_stevilka, ime, priimek, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            telefonska_stevilka=telefonska_stevilka,
            ime=ime,
            priimek=priimek
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, telefonska_stevilka, ime, priimek, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            telefonska_stevilka=telefonska_stevilka,
            ime=ime,
            priimek=priimek
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
