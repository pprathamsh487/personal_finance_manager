from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from ..forms.budget_entry_form import BudgetForm, BudgetEntryForm
from ..models import Category, BudgetEntry

class BudgetAndEntryCreateView(LoginRequiredMixin, View):
    template_name = 'budgeting/budget_form.html'

    def get(self, request, *args, **kwargs):
        # Create blank forms for GET request
        budget_form = BudgetForm()
        budget_entry_form = BudgetEntryForm()
        return render(request, self.template_name, {
            'budget_form': budget_form,
            'budget_entry_form': budget_entry_form,
        })

    def post(self, request, *args, **kwargs):
        # Handle the POST request and process both forms
        budget_form = BudgetForm(request.POST)
        
        # Get all category names and amounts from the request
        category_names = request.POST.getlist('category_name')
        amounts = request.POST.getlist('amount')

        if budget_form.is_valid() and category_names and amounts:
            # Save the budget form first
            budget = budget_form.save(commit=False)
            budget.user = request.user
            budget.save()

            entries = []  # Collect all budget entries to save later
            
            # Iterate over category names and amounts to create BudgetEntry instances
            for category_name, amount in zip(category_names, amounts):
                category_name = category_name.strip()
                amount = amount.strip()

                if category_name and amount:  # Ensure both are provided
                    # Get or create the category while associating it with the budget
                    category, created = Category.objects.get_or_create(
                        name=category_name,
                        budget=budget  # Ensure the budget is set when creating the category
                    )

                    # Create a BudgetEntry instance
                    budget_entry = BudgetEntry(
                        budget=budget,
                        user=request.user,
                        category=category,
                        amount=amount
                    )
                    entries.append(budget_entry)

            # Save all budget entries at once
            BudgetEntry.objects.bulk_create(entries)

            return redirect('budget_list')
        else:
            # Re-render the form with validation errors if not valid
            return render(request, self.template_name, {
                'budget_form': budget_form,
                'budget_entry_form': BudgetEntryForm(),  # Reset entry form for re-render
            })
