# email_sender/serializers.py

from rest_framework import serializers

class EmailSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=255)
    message = serializers.CharField()
    recipients = serializers.ListField(child=serializers.EmailField())
