from rest_framework import serializers

from ..models import Pastebin



class PublicPastebinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pastebin
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'date': {'read_only': True},
            'privacy': {'read_only': True},
        }

class PastebinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pastebin
        fields = '__all__'
        extra_kwargs = {
            'user': {'read_only': True},
            'date': {'read_only': True},
        }

class DateSerializerForm(serializers.Serializer):
    date1 = serializers.DateField()

