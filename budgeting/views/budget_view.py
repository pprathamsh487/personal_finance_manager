from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from ..models import Budget
from rest_framework.views import APIView
class BudgetView(TemplateView, APIView):
    template_name = 'budgeting/budget.html'
    
    def post(self, request):
        # Handle budget form submission
        categories = []
        amounts = []
        for key, value in request.POST.items():
            if key.startswith('category_'):
                categories.append(value)
            elif key.startswith('amount_'):
                amounts.append(value)

        # Save the budget categories and amounts to the database
        for category, amount in zip(categories, amounts):
            Budget.objects.create(user=request.user, category=category, amount=amount)

        return redirect('home')