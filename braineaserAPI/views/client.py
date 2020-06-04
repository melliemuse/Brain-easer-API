from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from braineaserAPI.models import Client
from django.contrib.auth.models import User

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    """ JSON serializer for client

    Arguments:
        serializers.HyperlinkedModelSerializer
    """

    class Meta:
        model = Client
        url = serializers.HyperlinkedIdentityField(
            view_name='clients',
            lookup_field='id'
        )
        fields = ('id', "user", 'inner_child_image')
        depth = 1



class Clients(ViewSet):

    def retrieve(self, request, pk=None):
        """
        Handles GET request for Client

        Returns:
            Response -- JSON serialized Client instance
        """

        try:
            client = Client.objects.get(pk=pk)
            serializer = ClientSerializer(
            client, context={'request': request})
            return Response(serializer.data)

        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """
        Handles GET request for Client list

        Returns:
            Response -- JSON of serialized Client list
        """

        client = Client.objects.all()
        user = self.request.query_params.get('user', None)
        print(request.auth.user.client.id)

        if user is not None:
            client = Client.objects.filter(id = request.auth.user.client.id)
            serializer = ClientSerializer(
            client, many=True, context={'request': request})
        else:
            client = Client.objects.all()
            serializer = ClientSerializer(
            client, many=True, context={'request': request})


        return Response(serializer.data)