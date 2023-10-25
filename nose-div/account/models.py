from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None , **extra_fields):
        """create and save new user"""
        if not email:
            raise ValueError("email address must not empty")
        user = self.model(username = username ,email = self.normalize_email(email) , **extra_fields)
        user.set_password(password)
        user.save(using= self._db)

        return user
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using= self._db)

        return user
    

class User(AbstractBaseUser, PermissionsMixin):
    email= models.EmailField(max_length=200)
    username= models.CharField(max_length=200, unique=True)
    last_login = models.DateTimeField(('last login'), blank=True, null=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_active = models.BooleanField(default=True)
    rate = models.PositiveIntegerField(default=0)
    age = models.PositiveIntegerField(null = True)
    image = models.ImageField(upload_to="/user/image", blank=True, null=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'

class Post(models.Model):
    title = models.CharField(max_length=100)
    caption = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    publish_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to="/post/image", blank=True, null=True)

    def __str__(self):
        return self.title