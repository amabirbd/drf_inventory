from rest_framework import serializers
from inventory.models import Inventory

class InventorySerilizer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'