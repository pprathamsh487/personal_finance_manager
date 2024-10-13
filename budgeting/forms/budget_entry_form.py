from django import forms
from ..models import Budget, BudgetEntry, Category

class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['name']
        labels = {
            'name': 'Budget Name'
        }

class BudgetEntryForm(forms.ModelForm):
    # category_names = forms.CharField(max_length=255, required=True, label='Category Names', widget=forms.Textarea)  # Allow input for multiple categories

    class Meta:
        model = BudgetEntry
        fields = ['amount']

    def save(self, budget=None, user=None, category_names=None, amounts=None, commit=True):
        if category_names and amounts:
            entries = []
            for category_name, amount in zip(category_names, amounts):
                # Create or get category by name
                category, created = Category.objects.get_or_create(name=category_name.strip(), budget=budget)

                # Create a new BudgetEntry instance
                entry = BudgetEntry(budget=budget, user=user, category=category, amount=amount)
                entries.append(entry)

            if commit:
                BudgetEntry.objects.bulk_create(entries)  # Save all entries at once

        return entries
