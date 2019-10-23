# Rest
import datetime

from django.utils.datastructures import MultiValueDictKeyError
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ParseError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# Models
from ..models import Pastebin
# Serializers
from .serializers import PastebinSerializer, PublicPastebinSerializer, DateSerializerForm


# For Public Users
#--------------------------------------------------------
class PublicPastebinCLView(ListCreateAPIView):
    serializer_class = PublicPastebinSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Pastebin.objects.filter(privacy=3)


class PublicPastebinListView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = PublicPastebinSerializer
    permission_classes = (AllowAny,)
    def get_queryset(self):
        return Pastebin.objects.filter(id=self.kwargs['pk']) & Pastebin.objects.filter(privacy=3)
#------------------------------------------------------------------------------------------------------------------!!!!!

# For Certain Users
#-------------------------------------------------------
class CertainPastebinLCView(ListCreateAPIView):
    serializer_class = PastebinSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Pastebin.objects.filter(privacy__in=[2,3])

    def perform_create(self, serializer):
        posted_data = serializer.validated_data
        posted_data['user_id'] = self.kwargs['pk']
        print(posted_data['user_id'])
        return serializer.save()


class CertainPastebinListView(ListAPIView):
    lookup_field = 'pk'
    serializer_class = PublicPastebinSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    def get_queryset(self):
        return Pastebin.objects.filter(id=self.kwargs['pk']) & Pastebin.objects.filter(privacy__in=[2,3])


class PasteByDate(GenericAPIView):
    queryset = Pastebin.objects.filter(privacy__in=[2,3])
    serializer_class = DateSerializerForm
    permissions = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        serializerform = self.get_serializer(data=request.data)
        if not serializerform.is_valid():
            raise ParseError(detail="No valid values")
        date1 = request.data['date1']
        pastbains = Pastebin.objects.filter(date=date1) & Pastebin.objects.filter(privacy__in=[2,3])
        if pastbains.exists():
            serializer = PublicPastebinSerializer(pastbains, many=True)
            return Response(serializer.data)

        return Response ({"Error": "This date doesn't match any element"})
#-----------------------------------------------------------------------------------------------------------------------


# For Private Users
#------------------------------------------------------------
class PrivatePastebinLCView(ListCreateAPIView):
    lookup_field = 'pk'
    serializer_class = PastebinSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Pastebin.objects.filter(user_id=self.kwargs['pk'])

    def perform_create(self, serializer):
        posted_data = serializer.validated_data
        posted_data['user_id'] = self.kwargs['pk']
        print(posted_data['user_id'])
        return serializer.save()


class PrivatePastebinRUDView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = PastebinSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Pastebin.objects.filter(user_id=self.kwargs['spk'])



