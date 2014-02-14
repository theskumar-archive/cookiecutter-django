# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import User

from users.models import User

class UserSerializer(serializers.ModelSerializer):

    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'full_name', 'first_name', 'last_name', 'email', 'date_joined', 'last_login', )
        read_only_fields = ('date_joined', 'last_login', )
