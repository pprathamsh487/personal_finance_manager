from django.urls import path
from .views.budget_view import BudgetView
urlpatterns = [
    
        path('set/', BudgetView.as_view(), name='setup_budget'),  # Budget setup page
        
]