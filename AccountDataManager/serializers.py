from rest_framework import serializers

from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id","username", "password")
        extra_kwargs = {
            "password": {
                "write_only": True,
                'style': {'input_type': 'password'}
                
            }
        }



        
        

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)









