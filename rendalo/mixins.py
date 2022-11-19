from django.db.models import QuerySet
from rest_framework.mixins import ListModelMixin
from rendalo.filters import Filter


class ListFilterModelMixin(ListModelMixin):

    @property
    def filter_class(self)->Filter:
        raise NotImplementedError

    def filter_queryset(self, queryset: QuerySet)-> QuerySet:
        filter = self.filter_class(queryset)
        for key, value in self.request.query_params.items():
            function = getattr(filter, f"by_{key}", None)
            if not callable(function):
                continue
            function(value)

        return filter.queryset
