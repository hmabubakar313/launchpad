from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager 


# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self,email,password,first_name,last_name,**extra_fields):
        if not email:
            raise ValueError('Email must be provided')
        if not password:
            raise ValueError('Password is not provided')
        
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        
        )
        user.set_password(password)
        
        user.save(using=self._db)
        
        return user
    

    def create_user(self,email,password,first_name,last_name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password,first_name,last_name,**extra_fields)
    
    
    
    def create_superuser(self,email,password,first_name,last_name,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,password,first_name,last_name,**extra_fields)
    
    

    
    
    
    
    
    
    
    


class User(AbstractUser,PermissionsMixin):
    username = models.CharField(max_length=100,unique=True,db_index=True)
    email = models.EmailField(unique=True,db_index=True,max_length=255)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  
    
    User = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'