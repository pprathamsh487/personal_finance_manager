from django.contrib.auth import views as auth_views
from django.urls import path
from .views.signup_view import SignUpView
from .views.home_view import *

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('home/', HomePageView.as_view(), name = 'home'),        # Home Page
    path('expenses/', ExpenseTrackingView.as_view(), name='track_expenses'),  # Expense tracking
    path('analytics/', AnalyticsView.as_view(), name='analytics')
]

