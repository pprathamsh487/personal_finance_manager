from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from expense_tracking.models import Expense
from budgeting.models import Budget
from expense_tracking.forms.expense_form import ExpenseForm

class ExpenseCreateView(View):
    def get(self, request, budget_id):
        budget = get_object_or_404(Budget, id=budget_id)
        form = ExpenseForm()
        context = {
            'form': form,
            'budget': budget
        }
        return render(request, 'expense_tracking/expense_form.html', context)

    def post(self, request, budget_id):
        budget = get_object_or_404(Budget, id=budget_id)
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.budget = budget
            expense.user_id = budget.user_id
            expense.save()

            return redirect('expense_list', budget_id=budget_id)
        
        context = {
            'form': form,
            'budget': budget
        }
        return render(request, 'expense_tracking/expense_form.html', context)
