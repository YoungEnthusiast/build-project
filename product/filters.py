import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import ProductOrder

class ProductOrderFilter(filters.FilterSet):
    start_date = DateFilter(field_name="date_ordered", lookup_expr='gte', label='Date Ordered')
    #end_date = DateFilter(field_name="date_ordered", lookup_expr='lte')

    class Meta:
        model = ProductOrder
        fields = ['id', 'product', 'order_status', 'payment_status']
