# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.request import Request
from django.db.models import QuerySet


class FilterBackend:

    def filter_queryset(self, request: Request, queryset: QuerySet, view)-> QuerySet:
        """
        Args:
            request (Request):
            queryset (QuerySet):
            view (mixins.ListFilterModelMixin):

        Returns:
            QuerySet: queryset filtered
        """       
        filter = view.filter_class(queryset)
        for key, value in request.query_params.items():
            function = getattr(filter, f"by_{key}", None)
            if not callable(function):
                continue
            function(value)

        return filter.queryset
