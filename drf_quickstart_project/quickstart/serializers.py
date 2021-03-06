from nntplib import GroupInfo
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# We use hyperlinked relations with `HyperlinkedModelSerializer`
# You can also use primary key and various other relationships, but
# hyperlinking is good restful design.

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
