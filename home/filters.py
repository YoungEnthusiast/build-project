import django_filters
from django_filters import CharFilter
from .models import Contact

class ContactFilter(django_filters.FilterSet):
    phone_number = CharFilter(field_name='phone_number', lookup_expr='icontains')
    #phone_number = CharFilter(field_name='phone_number', lookup_expr='iexact')

    class Meta:
        model = Contact
        fields = ['email', 'phone_number', 'status']
        labels = {
            'phone_number': "Phone Number Contains",
        }
