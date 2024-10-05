from django.views.generic import ListView
from ..models import Budget
from django.contrib.auth.mixins import LoginRequiredMixin
class BudgetForTrackingView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budgeting/budget_tracking_list.html'
    context_object_name = 'budgets'

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
