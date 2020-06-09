from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from braineaserAPI.models import Prompt

class PromptSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for Prompt

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Prompt
        url = serializers.HyperlinkedIdentityField(
            view_name='prompt',
            lookup_field='id'
        )
        fields = ('id', 'prompt')

class Prompts(ViewSet):
    def retrieve(self, request, pk=None):
        """
        Handles GET request for Prompts

        Returns:
            Response -- JSON serialized Prompt instance
        """

        try:
            prompt = Prompt.objects.get(pk=pk)
            serializer = PromptSerializer(prompt, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
   
    def list(self, request):
        """
        Handles GET requests for Prompts

        Returns:
            Response -- JSON serialized Prompt list
        """

        prompt = Prompt.objects.all()
        serializer = PromptSerializer(prompt, many=True, context={'request': request})
        return Response(serializer.data)