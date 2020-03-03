#from django.contrib.auth.models import User, Group
from rest_framework import serializers
from tutorial.quickstart.models import User


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']

# class SongsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Songs
#         fields = ("title", "artist")

class getuserserializer(serializers.Serializer):
    name=serializers.CharField()
    designation=serializers.CharField()


    # class Meta:
    #     model = User
    #     fields = ('name', "designation")