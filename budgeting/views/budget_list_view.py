from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Budget

class BudgetListView(LoginRequiredMixin, ListView):
    model = Budget
    template_name = 'budgeting/budget_list.html'
    context_object_name = 'budgets'

    def get_queryset(self):
        # Fetch unique budget names and their IDs for the logged-in user
        return Budget.objects.filter(user=self.request.user).values('id','name').distinct()

    