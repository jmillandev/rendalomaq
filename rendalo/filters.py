from django.db.models import QuerySet

class Filter:
    """
    If you wanna create a Filter class you need inherit from this and create methods like:
    ```python
    def by_name(self, name: str)-> QuerySet:
        self._queryset = self._queryset.filter(name=name)
        return self
    ``` 
    """
    _queryset: QuerySet

    def __init__(self, queryset: QuerySet) -> None:
        self._queryset = queryset

    @property
    def queryset(self) -> QuerySet:
        return self._queryset
