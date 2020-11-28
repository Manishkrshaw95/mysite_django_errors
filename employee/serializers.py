from rest_framework import serializers
from .models import Muser

class MuserSerializer(serializers.ModelSerializer):
    class Meta :
        model = Muser
        fields = ('name','age',)
