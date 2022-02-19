from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
#from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#from rest_framework.permissions import IsAuthenticated
# Create your views here.


#Reading all ToDo Lists
@api_view(['GET'])
#@authentication_classes([SessionAuthentication, BasicAuthentication])
#@permission_classes([IsAuthenticated])
def List(request):
    listobj = ListModel.objects.all()
    serializer = AppSerializer(listobj, many=True)
    return Response(serializer.data)


#Reading single ToDo List based on id
@api_view(['GET'])
def Post_Single_List(request, id):
    listobj = ListModel.objects.get(id=id)
    serializer = AppSerializer(listobj, many=False)
    return Response(serializer.data)


#Create a ToDo List
@api_view(['POST'])
def Post_List(request):
    listobj = ListModel.objects.all()
    serializer = AppSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#Update a ToDo List
@api_view(['POST'])
def Update_List(request, id):
    listobj = ListModel.objects.get(id=id)
    serializer = AppSerializer(instance=listobj, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#Delete a ToDo List
@api_view(['DELETE'])
def Delete_List(request, id):
    listobj = ListModel.objects.get(id=id)
    listobj.delete()
    return Response("Item is deleted.")
