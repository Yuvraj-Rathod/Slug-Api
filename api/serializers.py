from rest_framework import serializers
from api.models import Demo_Model

class Demo_serializer(serializers.ModelSerializer):
    class Meta:
        model = Demo_Model
        fields = ('__all__')
        lookup_fields = 'name'
        extra_kwargs = {
            'url':{'lookup_fields':'name'}
        }