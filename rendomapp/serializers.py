from rest_framework import serializers
from .models import  Users


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id','uid','password','first_name','last_name','username','email','avatar','gender','phone_number','social_insurance_number','date_of_birth']

