from django import forms
from expense_tracking.models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category','description', 'amount']  # Add other fields if necessary
