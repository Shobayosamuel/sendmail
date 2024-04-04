from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import EmailSerializer
from .utils import send_email

class SendEmailView(APIView):
    def post(self, request):
        serializer = EmailSerializer(data=request.data)
        if serializer.is_valid():
            subject = serializer.validated_data['subject']
            message = serializer.validated_data['message']
            recipients = serializer.validated_data['recipients']
            send_email(subject, message, recipients)
            return Response({"message": "Email sent successfully."}, status=200)
        return Response(serializer.errors, status=400)
