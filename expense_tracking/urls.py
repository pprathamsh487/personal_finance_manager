from django.urls import path
from .views.expense_create_view import ExpenseCreateView
from .views.expense_list_view import ExpenseListView

urlpatterns = [
    path('list/<int:budget_id>', ExpenseListView.as_view(), name='expense_list'),
    path('create/<int:budget_id>', ExpenseCreateView.as_view(), name='expense_create'),
]
