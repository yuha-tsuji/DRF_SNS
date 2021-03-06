from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from core.models import Message
from api_dm import seriakizers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics, authentication, permissions


# Create your views here.

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = seriakizers.MessageSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.queryset.filter(sender=self.request.user)

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)

class InboxListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = seriakizers.MessageSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(receiver=self.request.user)
