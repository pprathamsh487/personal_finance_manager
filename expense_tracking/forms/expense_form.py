from django import forms
from ..models import Expense
from budgeting.models import Category

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['category', 'amount']  # Specify fields to be displayed in the form

    def __init__(self, *args, **kwargs):
        budget = kwargs.pop('budget', None)
        super().__init__(*args, **kwargs)
        if budget:
            # Limit the categories based on the selected budget
            self.fields['category'].queryset = Category.objects.filter(budget=budget)

    category = forms.ModelChoiceField(queryset=Category.objects.none(), widget=forms.Select(attrs={'class': 'form-control'}))
    amount = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
