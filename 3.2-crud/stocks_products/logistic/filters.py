from django.db.models import Q
import django_filters
from logistic.models import Stock


class StockFilter(django_filters.FilterSet):
    product = django_filters.CharFilter(method='filter_search')

    @staticmethod
    def filter_search(queryset, name, value):
        return queryset.filter(
            Q(products__title__icontains=value) |
            Q(products__description__icontains=value)
        )

    class Meta:
        model = Stock
        fields = ['product']
