from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from items.models import Item
from api.serializers import ItemSerializer 
import django_filters


class ItemFilter(django_filters.FilterSet):
	min_revenue = django_filters.NumberFilter(name='revenue', lookup_type='gte')
	max_revenue = django_filters.NumberFilter(name='revenue', lookup_type='lte')
	class Meta:
		model = Item
		fields = ['item_type', 'year', 'revenue', 'max_revenue', 'min_revenue']

class ItemViewSet(viewsets.ModelViewSet):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = ItemFilter
