from rest_framework import serializers
from .models import Purchase, Store

class Rest_Purchase(serializers.ModelSerializer):

    class Meta:

        model = Purchase
        fields = '__all__'


class Rest_Store(serializers.ModelSerializer):

    class Meta:

        model = Store
        fields = '__all__'
