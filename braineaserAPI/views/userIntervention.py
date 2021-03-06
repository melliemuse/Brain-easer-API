from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from braineaserAPI.models import UserIntervention, Client, Intervention

class UserInterventionSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for UserIntervention

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = UserIntervention
        url = serializers.HyperlinkedIdentityField(
            view_name='user_intervention',
            lookup_field='id'
        )
        fields = ('id', 'timestamp', 'anxiety_score', 'intervention', 'client', 'description')
        depth = 1

class UserInterventions(ViewSet):
    def retrieve(self, request, pk=None):
        """
        Handles single GET request for UserIntervention
        
        Returns:
            Response -- JSON serialized UserIntervention Instance
        """
        
        try:
            user_intervention = UserIntervention.objects.get(pk=pk)
            serializer = UserInterventionSerializer(user_intervention, context={'request': request})
            return Response(serializer.data)
            
        except Exception as ex:
            return HttpResponseServerError(ex)
    def list(self, request):
        """
        Handles GET request for userIntervention

        Returns:
            Response -- JSON of serialized userIntervention list
        """

        user_intervention = UserIntervention.objects.all()
        user = self.request.query_params.get('user', None)
        

        if user is not None:
            user_intervention = UserIntervention.objects.filter(client=request.auth.user.client.id)
            serializer = UserInterventionSerializer(user_intervention, many=True, context={'request': request})
            return Response(serializer.data)

        else:
            user_intervention = UserIntervention.objects.all()
            serializer = UserInterventionSerializer(user_intervention, many=True, context={'request': request})
            return Response(serializer.data)



    def create(self, request):
        """
        Handle POST request for User Intervention

        Returns:
            Response -- JSON serialized User Intervention Instance
        """
        current_user = request.auth.user.client.id
        client = Client()
        user_intervention = UserIntervention()

        client.id = current_user
        user_intervention.client_id = client.id
        user_intervention.intervention_id = request.data['intervention']
        user_intervention.anxiety_score = request.data['anxiety_score']
        user_intervention.description = request.data['description']

        user_intervention.save()

        serializer = UserInterventionSerializer(user_intervention, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        Handles PUT requests for individual User Intervention item
        Returns:
            Response -- Empty body with 204 status code
        """
        # current_user = request.auth.user.client.id
        user_intervention = UserIntervention.objects.get(pk=pk)
        intervention = Intervention.objects.get(id=request.data["intervention"])

        user_intervention.anxiety_score = request.data["anxiety_score"]
        user_intervention.intervention = intervention
        user_intervention.description = request.data["description"]
        # user_intervention.client_id = current_user

        user_intervention.save()


        return Response({}, status=status.HTTP_204_NO_CONTENT)