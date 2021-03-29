import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import WalletHistory


class WalletHistoryFilter(filters.FilterSet):
    start_date = DateFilter(field_name="date_recorded", lookup_expr='gte', label='Date')

    class Meta:
        model = WalletHistory
        fields = ['amount_debited', 'amount_credited']
