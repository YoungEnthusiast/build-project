import django_filters
from django_filters import CharFilter, DateFilter
from .models import CementOrder

class CementOrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_ordered", lookup_expr='gte')
    #end_date = DateFilter(field_name="date_ordered", lookup_expr='lte')

    class Meta:
        model = CementOrder
        fields = ['id', 'cement', 'order_status', 'payment_status']
