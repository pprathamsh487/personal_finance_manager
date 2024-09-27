from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import Budget
class BudgetCreateView(LoginRequiredMixin, CreateView):
    model = Budget
    # form_class = BudgetForm  # Use your form
    template_name = 'budgeting/budget_form.html'
    fields = ['name']  # Add the fields you want to include in the form (e.g., 'name', 'total_amount')
    success_url = reverse_lazy('budget_list')

    def form_valid(self, form):
        # Set the user before saving the form
        form.instance.user = self.request.user
        return super().form_valid(form)  # Save the entry and call the parent method

    def get_success_url(self):
        # Redirect to the budget list view after successfully creating the budget
        return reverse_lazy('budget_list')