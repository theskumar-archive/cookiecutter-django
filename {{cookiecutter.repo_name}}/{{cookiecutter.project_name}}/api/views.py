# -*- coding: utf-8 -*-
from __future__ import unicode_literals, division

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.reverse import reverse

from users.models import User

from .serializers import UserSerializer

@api_view(('GET',))
def api_root(request, format=None):
    '''
    List of api endpoints for **Type** Project.

    ### Authentication

    Visit `auth-token`'s url to obtain a JSON-Web Token. `BasicAuth` is also supported.

    ### Errors

    By default all error responses will include a key `details` in the body of
    the response.
    '''
    return Response({
        'api_root': reverse('api_root', request=request, format=format),
        'user': reverse('api_user', request=request, format=format),
        'signup': reverse('api_user_signup', request=request, format=format),
        'auth-token': reverse('api_auth_token', request=request, format=format),
    })


class UserRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    '''
    Endpoint to get and update profile of a `User`.
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


@api_view(('POST',))
@permission_classes((AllowAny,))
def user_signup(request, format=None):
    '''
    Enpoint to signup a new user using email, password and other details.
    '''
    context = {
        'details': 'Not Implemented'
    }
    return Response(context)
