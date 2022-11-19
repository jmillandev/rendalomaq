from django.db.models import QuerySet

class Filter:
    def __init__(self, queryset: QuerySet) -> None:
        self._queryset = queryset

    @property
    def queryset(self) -> QuerySet:
        return self._queryset
