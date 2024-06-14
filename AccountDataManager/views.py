from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import (UserSerializer, ChangePasswordSerializer)
                           


@api_view(http_method_names=["POST"])
def SaveLoginInfo(request):
    data = request.data
    serializer = UserSerializer(data=data)

    if serializer.is_valid():
        serializer.save(password=make_password(data["password"]))
        return Response(data={"message":"Account Created",
                              "data":serializer.data}, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)



@api_view(http_method_names=["GET"])
def getusers(request):
    queryset = User.objects.all()
    serializer = UserSerializer(instance=queryset, many=True)
    return Response(data=serializer.data)


@api_view(http_method_names=["GET","PUT"])
def changePassword(request,pk):

    if request.method == "GET":
        user = User.objects.get(id=pk)
        serializer = UserSerializer(instance=user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    
    elif request.method == "PUT":
        user = User.objects.get(id=pk) 
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.data["old_password"]
            if not user.check_password(old_password):
                return Response(data={"message":"Wrong Password"})
            else:
                new_password = serializer.data["new_password"]
                confirm_password = serializer.data["confirm_password"]
                if new_password == old_password:
                    return Response(data={"message":"U Entered Old Password"})
                elif new_password != confirm_password:
                    return Response(data={"message":"Wrong Confirm Password"})
                else:
                    user.set_password(new_password)
                    user.save()
                    return Response(data={"message":"Password Updated"})

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


def login(request):
    pass


