from rest_framework import serializers

from database import models



class UserInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.UserInformation
        fields = ("bloodType", "name", "mobile", "govern",
                   "state", "Card_number",
                   "age","gender", "user")
        

class UpdateInformationSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)