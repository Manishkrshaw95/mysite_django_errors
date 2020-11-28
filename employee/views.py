from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.response import Response
from .serializers import MuserSerializer
from employee.models import Muser

# Create your views here.
class userViewSet(generics.RetrieveAPIView):
    """
    A viewset for viewing and editing user instances.
    """
    #serializer_class = MuserSerializer

    def get(self, request):   

        shw = Muser.objects.filter(pk!=None)

        print (shw._data)#(MuserSerializer(data=shw).data)
        return Response(MuserSerializer(shw, many=True)).data
    





