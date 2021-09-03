from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django_google_maps.fields import AddressField, GeoLocationField

class Memory(models.Model):
    name = models.CharField(max_length=100)
    address = AddressField(max_length=100)
    geolocation = GeoLocationField(blank=True)
    comment = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        return self.address

# class Profile(models.Model):
#     user = models.OneToOneField(User, null=True, on_delete=CASCADE)
#     profile_pic = models.ImageField(null=True, blank=True, upload_to ="image/profile/")

#     def __str__(self):
#         return str(self.user)