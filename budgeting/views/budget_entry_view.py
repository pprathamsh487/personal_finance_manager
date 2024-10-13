from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from ..models import  BudgetEntry, Budget, Category
from ..forms.budget_entry_form import BudgetEntryForm
from django.urls import reverse_lazy
class BudgetEntryCreateView(LoginRequiredMixin, CreateView):
    model = BudgetEntry
    template_name = 'budgeting/budget_entry_form.html'
    form_class = BudgetEntryForm

    success_url = reverse_lazy('budget_list')
    
    def dispatch(self, request, *args, **kwargs):
        # Get the budget instance based on budget_id from the URL
        self.budget = get_object_or_404(Budget, id=kwargs['budget_id'])
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        # Set the logged-in user before saving the form
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        # Capture and process the POST request
        form = self.get_form()  # Get the form with the POST data
        # Get or create the category based on the category name provided in the form
        category_name = form.data['category']
        budget = self.budget
        category, created = Category.objects.get_or_create(name=category_name, budget = budget)
        if form.is_valid():
            # Set the user and budget for the entry
            form.instance.user = self.request.user
            form.instance.budget = self.budget
            form.instance.category = category  # Set the category for the entry

            return self.form_valid(form)  # Save the form and handle redirect
        else:
            # If form is invalid, re-render the form with errors
            return self.form_invalid(form)