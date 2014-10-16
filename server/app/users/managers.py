from django.contrib.auth.models import BaseUserManager
from django.utils import timezone


class UserManager(BaseUserManager):

    def _creator(
        self, email, password, is_staff, is_superuser,
        first_name, last_name, **extra_fields
    ):
        now = timezone.now()
        if not email:
            raise ValueError('Email is required')
        email = self.normalize_email(email)
        user = self.model(
            email=email, first_name=first_name, last_name=last_name,
            is_staff=is_staff, is_superuser=is_superuser,
            date_joined=now, last_login=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(
        self, email, password, first_name, last_name, **extra_fields
    ):
        return self._creator(
            email, password, False, False, first_name, last_name, **extra_fields
        )

    def create_staff(
        self, email, password, first_name, last_name, **extra_fields
    ):
        return self._creator(
            email, password, True, False, first_name, last_name, **extra_fields
        )

    def create_superuser(
        self, email, password, first_name, last_name, **extra_fields
    ):
        return self._creator(
            email, password, True, True, first_name, last_name, **extra_fields
        )
