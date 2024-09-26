from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from ..forms.signup_form import CustomUserCreationForm

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')  # Redirect to login after signup
    template_name = 'registration/signup.html'
