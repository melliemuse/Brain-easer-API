from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for User

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = User
        url = serializers.HyperlinkedIdentityField(
            view_name='user',
            lookup_field='id'
        )

    fields = ('id', 'first_name', 'last_name', 'email')

class Users(ViewSet):

    def retrieve(self, request, pk=None):
        """
        Handles GET requests for single User

        Returns:
            Response -- JSON serialized user instance
        """

        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
        Handles GET request to Users resource

        Returns:
            Response -- JSON serialized list of users
        """

        users = User.objects.all()

        serializer = UserSerializer(users, many=True, context={'request': request})

        return Response(serializer.data)