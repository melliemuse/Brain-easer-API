from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from braineaserAPI.models import BaselineAnxietyScore, Client

class BaselineAnxietyScoreSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for Baseline Anxiety Score

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = BaselineAnxietyScore
        url = serializers.HyperlinkedIdentityField(
            view_name='baselineAnxietyScore',
            lookup_field='id'
        )
        fields = ('id', 'client', 'anxiety_score', 'timestamp', 'description', 'client')
        depth = 1

class BaselineAnxietyScores(ViewSet):
    def retrieve(self, request, pk=None):
        """
        Handles single GET request for Baseline Anxiety Score
        
        Returns:
            Response -- JSON serialized Baseline Anxiety Score Instance
        """

        try:
            baseline_score = BaselineAnxietyScore.objects.get(pk=pk)
            serializer = BaselineAnxietyScoreSerializer(baseline_score, context={'request': request})
            return Response(serializer.data)
            
        except Exception as ex:
            return HttpResponseServerError(ex)
    def list(self, request):
        """
        Handles GET request for Baseline Anxiety Score list

        Returns:
            Response -- JSON serialized Baseline Anxiety Score list
        """

        baseline_score = BaselineAnxietyScore.objects.all()
        user = self.request.query_params.get('user', None)

       
        if user is not None:
            baseline_score = BaselineAnxietyScore.objects.filter(client=request.auth.user.client.id)
            serializer = BaselineAnxietyScoreSerializer(baseline_score, many=True, context={'request': request})
            return Response(serializer.data)
       
        else: 
            baseline_score = BaselineAnxietyScore.objects.all()
            serializer = BaselineAnxietyScoreSerializer(baseline_score, many=True, context={'request': request})
            return Response(serializer.data)

    def create(self, request):
        """
        Handle POST request for Baseline Anxiety

        Returns:
            Response -- JSON serialized Baseline Anxiety Instance
        """
        current_user = request.auth.user.client.id
        client = Client()
        baseline_score = BaselineAnxietyScore()

        client.id = current_user
        baseline_score.client_id = client.id
        baseline_score.anxiety_score = request.data['anxiety_score']
        baseline_score.description = request.data['description']

        baseline_score.save()

        serializer = BaselineAnxietyScoreSerializer(baseline_score, context={'request': request})
        return Response(serializer.data)