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
        fields = ('id', 'user', 'inner_child_image')


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

        # current_client=request.query_params.get('self', False)

        client=Client.objects.all()

        serializer = ClientSerializer(
        client, many=True, context={'request': request})

        return Response(serializer.data)