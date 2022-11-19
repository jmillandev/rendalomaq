from rest_framework.mixins import ListModelMixin
from rendalo.backends import FilterBackend
from rendalo.filters import Filter


class ListFilterModelMixin(ListModelMixin):
    filter_backends = (FilterBackend,)

    @property
    def filter_class(self)->Filter:
        raise NotImplementedError
