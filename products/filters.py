import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import UserOrder

class UserOrderFilter(filters.FilterSet):
    start_date = DateFilter(field_name="date_Ordered", lookup_expr='gte', label='Date Ordered')

    class Meta:
        model = UserOrder
        fields = ['order_Id', 'product', 'order_Status', 'payment_Status']

class UserOrderFilter2(filters.FilterSet):
    start_date = DateFilter(field_name="date_Ordered", lookup_expr='gte', label='Date Ordered')
    #end_date = DateFilter(field_name="date_ordered", lookup_expr='lte')

    class Meta:
        model = UserOrder
        fields = ['order_Id', 'product', 'order_Status']
