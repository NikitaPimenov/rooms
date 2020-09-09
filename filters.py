import django_filters
from .models import Room


class RoomFilter(django_filters.FilterSet):
    CHOICES = (
        ('ascending', 'По возрастанию номера комнаты'),
        ('descending', 'По убыванию номера комнаты')
    )
    ordering = django_filters.ChoiceFilter(label='Сортировка', choices=CHOICES, method='filter_by_ordering')

    class Meta:
        model = Room
        fields = ('floor', 'capacity')

    def filter_by_ordering(self, queryset, name, value):
        expression = 'name' if value == 'ascending' else '-name'
        return queryset.order_by(expression)
