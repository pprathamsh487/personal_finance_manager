from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import  BudgetEntry
from django.urls import reverse_lazy
class BudgetEntryCreateView(LoginRequiredMixin, CreateView):
    model = BudgetEntry
    template_name = 'budgeting/budget_entry_form.html'
    fields = ['budget', 'category', 'amount']

    success_url = reverse_lazy('budget_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)