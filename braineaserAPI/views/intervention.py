from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from braineaserAPI.models import Intervention

class InterventionSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for Intervention

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Intervention
        url = serializers.HyperlinkedIdentityField(
            view_name='intervention',
            lookup_field='id'
        )
        fields = ('id', 'name', 'timestamp', 'description', 'instructions', 'detailed_info')

class Interventions(ViewSet):
    def retrieve(self, request, pk=None):
        """
        Handles single GET request for Intervention
        
        Returns:
            Response -- JSON serialized Intervention Instance
        """

        try:
            intervention = Intervention.objects.get(pk=pk)
            serializer = InterventionSerializer(intervention, context={'request': request})
            return Response(serializer.data)
            
        except Exception as ex:
            return HttpResponseServerError(ex)
