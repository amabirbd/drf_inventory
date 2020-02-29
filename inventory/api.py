from inventory.models import Inventory
from rest_framework import viewsets, permissions
from .serializers import InventorySerilizer

class InventoryViewSet(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    permission_classes = {
        permissions.IsAuthenticatedOrReadOnly
    }
    serializer_class = InventorySerilizer