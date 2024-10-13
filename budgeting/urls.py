# urls.py
from django.urls import path
from .views.budget_detail_view import BudgetDetailView
from .views.budget_list_view import BudgetListView
from .views.create_budget_view import BudgetAndEntryCreateView
from .views.budget_tracking_view import BudgetForTrackingView

urlpatterns = [
    path('list/', BudgetListView.as_view(), name='budget_list'),
    path('detail/<int:pk>/', BudgetDetailView.as_view(), name='budget_detail'),
    path('create/', BudgetAndEntryCreateView.as_view(), name='budget_and_entry_create'),  # For creating a new budget
    # path('entry/add/<int:budget_id>/', BudgetEntryCreateView.as_view(), name='budget_entry_create'),  # For adding entries to an existing budget
    path('track/', BudgetForTrackingView.as_view(), name='budget_tracking'),
]