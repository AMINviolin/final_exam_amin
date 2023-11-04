from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,BaseUserManager,PermissionsMixin


class CustomeBaseUserManager(BaseUserManager):
    def email_norm(self, email):
        email = str(email)
        if email.strip() == False or not email:
            raise ValueError('Your email is false')
        return email


    def create_user(self, email, password, **extra_fields):
        email = self.email_norm(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser should has staff:true')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser should has is.superuser:true')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username  = models.CharField(max_length=100)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomeBaseUserManager()

class Profile(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="user",default="user.png")
    phone = models.IntegerField(blank=True,null=True)
    address = models.CharField(max_length=10)

    def __str__(self):
        return self.user.email