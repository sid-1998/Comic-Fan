from django.db import models
from django.contrib import auth
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
     def __str__(self):
         return "@{}".format(self.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User)

    gender = models.CharField(max_length=8)
    profile_pic = models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return "@{}".format(self.user.username)
