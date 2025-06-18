from .models import MenuItemClass
from rest_framework import serializers

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItemClass
        fields = ['id', 'title', 'price', 'inventory']
        extra_kwargs = {
            'price': {'min_value' : 2},
            'inventory': {'min_value' : 0}
        }