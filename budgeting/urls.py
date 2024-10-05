# urls.py
from django.urls import path
from .views.budget_detail_view import BudgetDetailView
from .views.budget_list_view import BudgetListView
from .views.create_budget_view import BudgetCreateView
from .views.budget_entry_view import BudgetEntryCreateView
from .views.budget_tracking_view import BudgetForTrackingView

urlpatterns = [
    path('list/', BudgetListView.as_view(), name='budget_list'),
    path('detail/<int:pk>/', BudgetDetailView.as_view(), name='budget_detail'),
    path('create/', BudgetCreateView.as_view(), name='budget_create'),
    path('entry/create/', BudgetEntryCreateView.as_view(), name='budget_entry_create'),
    path('track/', BudgetForTrackingView.as_view(), name='budget_tracking'),
]
