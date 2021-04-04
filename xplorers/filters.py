import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import ProductWalletHistorie


class ProductWalletHistorieFilter(filters.FilterSet):
    start_date = DateFilter(field_name="date_recorded", lookup_expr='gte', label='Date')

    class Meta:
        model = ProductWalletHistorie
        fields = ['amount_debited', 'amount_credited']
