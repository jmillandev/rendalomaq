from django.db.models import Manager
from django.db.models import Avg

class ProductManager(Manager):
    
    def get_price_avg(self)->float:
        """Return the avg of the product prices"""
        return self.aggregate(Avg('price'))['price__avg']
