from django.conf import settings
from django.db import models
from . import Budget
from ..models.category import Category
class BudgetEntry(models.Model):
    budget = models.ForeignKey(Budget, related_name='entries', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Link category to Category model
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        db_table = 'BUDGET_ENTRY'

    def __str__(self):
        return f'{self.category.name} - {self.amount}'
