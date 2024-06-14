from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from database import models
from .serializers import UserInformationSerializer, UpdateInformationSerializer
                           


@api_view(http_method_names=["POST"])
def saveUserInformation(request):
    serializer = UserInformationSerializer(data=request.data)
    if serializer.is_valid():
        user_info= models.UserInformation.objects.create(
            user = User.objects.get(id=request.data["user"]),
            bloodType = request.data["bloodType"],
            name = request.data["name"],
            mobile = request.data["mobile"],
            govern = request.data["govern"],
            state = request.data["state"],
            Card_number = request.data["Card_number"],
            # date_of_donation = request.data["date_of_donation"],
            age = request.data["age"],
            gender = request.data["gender"]
        )
        

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



@api_view(http_method_names=["GET","PUT"])
def updateInformation(request):
    try:
        user = User.objects.get(id=request.data["user"])
        user_information = models.UserInformation.objects.get(user=user)

    except ObjectDoesNotExist:

        return Response(data={"message": "NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND) 
    
    if request.method == "GET":
        serializer = UserInformationSerializer(instance=user_information, many=False)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        password = request.data["password"]

        if user.check_password(password):
            serializer = UserInformationSerializer(instance=user_information, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(data={"message": "Wrong Password!"}, status=status.HTTP_401_UNAUTHORIZED)

    
    
@api_view(http_method_names=["GET", "DELETE"])
def deleteUser(request):
    try:
        user = User.objects.get(id=request.data["user"])
    
    except ObjectDoesNotExist:

        return Response(data={"message": "NOT FOUND!"}, status=status.HTTP_404_NOT_FOUND) 

    user.delete()
    return Response(data={"messgae": "Account Deleted"}, status=status.HTTP_204_NO_CONTENT)


    



        