from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Budget

class BudgetDetailView(LoginRequiredMixin, DetailView):
    model = Budget
    template_name = 'budgeting/budget_detail.html'
    context_object_name = 'budget'

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user)
