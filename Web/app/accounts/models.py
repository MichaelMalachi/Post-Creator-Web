# файл app/accounts/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class WebUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class WebUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    dateOfBirth = models.DateField()
    gender = models.CharField(max_length=10)
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    objects = WebUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['dateOfBirth', 'gender', 'role']

    def __str__(self):
        return self.email
