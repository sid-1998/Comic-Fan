from django.db import models
from django.contrib import auth
# Create your models here.
class User(auth.models.User,auth.models.PermissionsMixin):
     def __str__(self):
         return "@{}".format(self.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    user1= models.OneToOneField(User)

    def __str__(self):
        return "@{}".format(self.user.username)
