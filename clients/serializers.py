from rest_framework import serializers
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user']


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required = True)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'password2', 'email']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'error': 'Password does not match.'})
        
        if User.objects.filter(email = email).exists():
            raise serializers.ValidationError({'error': 'Email already exists.'})
    
        account = User.objects.create(username = username, email = email)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
    


class UserLoginSerializer(serializers.Serializer):
    username =serializers.CharField(required = True)
    password =serializers.CharField(required = True)