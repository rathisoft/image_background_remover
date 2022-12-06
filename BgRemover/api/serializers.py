from rest_framework import serializers
from ..models import Image
'''
A single dot means that the module or package referenced is in the same directory as the current location. 
Two dots mean that it is in the parent directory of the current location, in other words the directory above. 
Three dots mean that it is in the grandparent directory, and so on.
'''
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'img')