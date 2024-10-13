from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView
from ..models import Expense
from budgeting.models import Budget
from ..forms.expense_form import ExpenseForm  # Assuming you have the form for expense
from django.contrib.auth.mixins import LoginRequiredMixin
class ExpenseCreateView(LoginRequiredMixin, CreateView):
    model = Expense
    form_class = ExpenseForm
    template_name = 'expense_tracking/expense_form.html'

    def get_form_kwargs(self):
        # Get the current budget ID from the URL or request
        kwargs = super().get_form_kwargs()
        budget_id = self.kwargs.get('budget_id')  # Assume the budget ID is passed in the URL
        budget = get_object_or_404(Budget, id=budget_id)
        kwargs['budget'] = budget  # Pass the budget to the form for filtering categories
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.budget = form.cleaned_data['budget']
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to a page showing the expenses for the current budget
        return reverse_lazy('expense_list', kwargs={'budget_id': self.object.budget.id})
