from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionMixin

class User(AbstractBaseUser, PermissionMixin):
    email = models.EmailField(max_length = 250, unique = True)
    name = models.models.CharField(max_length = 50)
    is_active = models.Boolean_field(max_length = 255, unique = True)
    is_staff = models.BooleanField(default = False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        return self.name
    
    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email
