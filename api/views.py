from api.models import Phone
from rest_framework import status
from api.serializers import PhoneSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
class PhoneList(APIView):
    """
    get: List all phones
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        phones = Phone.objects.all()
        serializer = PhoneSerializer(phones, many=True)
        return Response(serializer.data)

class SetPhoneRating(APIView):
    """
    post: Create a new phone rating.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetPhoneRating(APIView):
    """
    get: Retrieve rating data for a phone.
    """
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, phoneHash):
        try:
            phone = Phone.objects.filter(phoneHash=phoneHash)
        except Phone.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if len(phone) == 0:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            phone = phone.order_by('-created')[0]
            if request.method == 'GET':
                serializer = PhoneSerializer(phone)
                return Response(serializer.data)
