from django.db import models

# Create your models here.
# class Songs(models.Model):
#     # song title
#     title = models.CharField(max_length=255, null=False)
#     # name of artist or group/band
#     artist = models.CharField(max_length=255, null=False)

#     def __str__(self):
#         return "{} - {}".format(self.title, self.artist)

class User(models.Model):

    id = models.IntegerField(null=False,primary_key=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)

    class Meta:
        db_table = 'user'