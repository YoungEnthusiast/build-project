import django_filters as filters
from django_filters import CharFilter, DateFilter
from .models import Subscription

class SubscriptionFilter(filters.FilterSet):
    start_date = DateFilter(field_name="date_Activated", lookup_expr='gte', label='Date Activated')
    end_date = DateFilter(field_name="subscription_Ends", lookup_expr='gte', label='Subscription Ends')

    # class Meta:
    #     model = Subscription
    #     fields = ['advert_Type']
