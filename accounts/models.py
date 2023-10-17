from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,BaseUserManager,PermissionsMixin


class CustomeBaseUserManager(BaseUserManager):
    def id_norm(self, id_code):
        id_code = str(id_code)
        if len(id_code) != 10 or id_code.strip() == False:
            raise ValueError('Your id is false')
        return id_code


    def create_user(self, id_code, password, **extra_fields):
        id_code = self.id_norm(id_code)
        user = self.model(id_code=id_code, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, id_code, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser should has staff:true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser should has is.superuser:true')
        return self.create_user(id_code, password, **extra_fields)


class CustomeUser(AbstractBaseUser, PermissionsMixin):
    id_code = models.IntegerField(unique=True)
    username  = models.CharField(max_length=100, unique=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'id_code'
    REQUIRED_FIELDS = []

    objects = CustomeBaseUserManager()

