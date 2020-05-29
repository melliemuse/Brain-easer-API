from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from braineaserAPI.models import BaselineAnxietyScore

class BaselineAnxietyScoreSerializer(serializers.HyperlinkedModelSerializer):
    """
    JSON serializer for Baseloine Anxiety Score

    Arguments:
        serializers.HyperlinkedModelSerializer
    """
    class Meta:
        model = BaselineAnxietyScore
        url = serializers.HyperlinkedIdentityField(
            view_name='baselineAnxietyScore',
            lookup_field='id'
        )
        fields = ('id', 'client', 'anxietyScore', 'timestamp', 'description')

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
