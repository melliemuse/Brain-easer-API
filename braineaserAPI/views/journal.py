from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from braineaserAPI.models import Journal, Client, Prompt

class JournalSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for Journal

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = Journal
        url = serializers.HyperlinkedIdentityField(
            view_name="journal",
            lookup_field="id"
        )
        fields = ('id', 'client', 'prompt', 'entry')
        depth = 1

class Journals(ViewSet):
    def retrieve(self, request, pk=None):
        """
        Handles GET request for Journal

        Returns:
            Response JSON serialized Journal instance
        """
    
        try: 
            journal = Journal.objects.get(pk=pk)
            serializer = JournalSerializer(journal, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
        
    def list(self, request):
        """
        Handles GET request for Journal

        Returns:
            Response JSON serialized Journal list
        """
        
        journal = Journal.objects.all()
        user = self.request.query_params.get('user', None)
        
        if user is not None:
            journal = Journal.objects.filter(client=request.auth.user.client.id)
            serializer = JournalSerializer(journal, many=True, context={'request': request})
            return Response(serializer.data)
        else:
            journal = Journal.objects.all()
            serializer = JournalSerializer(journal, many=True, context={'request': request})
            return Response(serializer.data)
    
    def create(self, request):
        """
        Handles POST request for Journal

        Returns:
            Response JSON serialized Journal instance
        """

        current_user = request.auth.user.client.id
        client = Client()
        prompt = Prompt()
        journal = Journal()

        client.id = current_user
        prompt.id = request.data['prompt']
        journal.client_id = client.id
        journal.entry = request.data['entry']
        journal.prompt = prompt

        journal.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    