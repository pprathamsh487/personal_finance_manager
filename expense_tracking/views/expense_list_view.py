from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Expense
from budgeting.models import Budget

class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    template_name = 'expenses/expense_list.html'
    context_object_name = 'expenses'

    def get_queryset(self):   # Gives the list of budgest for that user
        budget_id = self.kwargs['budget_id']
        return Expense.objects.filter(user=self.request.user, budget_id=budget_id)

    def get_context_data(self, **kwargs):   #provides the details of a specific budget that is selcted
        context = super().get_context_data(**kwargs)
        budget_id = self.kwargs['budget_id']
        context['budget'] = Budget.objects.get(id=budget_id)
        return context
