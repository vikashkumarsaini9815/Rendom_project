from django.shortcuts import render

# Create your views here.


from .models import Users
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status



@api_view(['GET','POST'])
def employe (request):

    if request.method == "POST":
        serializer = UserSerializer(data = request.data)
      
        if serializer.is_valid():
            for ele in range(10):
                serializer.save()
                response = {"Insert_Data":"your data has been inserted 10 times "}
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    else:
        respons = []
        return Response(respons)
    
