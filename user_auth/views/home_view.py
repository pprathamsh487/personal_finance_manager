from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class ExpenseTrackingView(TemplateView):
    template_name = 'expenses.html'

class AnalyticsView(TemplateView):
    template_name = 'analytics.html'
