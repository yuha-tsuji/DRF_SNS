from rest_framework import authentication, permissions
from rest_framework import viewsets

from core import ownpermission
from core.models import Tweet

from api_tweet import serializers

class TweetViewSet(viewsets.ModelViewSet):

    queryset = Tweet.objects.all()
    serializer_class = serializers.TweetSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, ownpermission.TweetPermission)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)