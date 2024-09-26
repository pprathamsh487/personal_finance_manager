from django.shortcuts import render
from django.views.generic import TemplateView

class BudgetView(TemplateView):
    template_name = 'budgeting/budget.html'