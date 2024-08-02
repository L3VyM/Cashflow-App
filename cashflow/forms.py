from django import forms
from .models import CashFlowSection, Transaction, CashFlowStatement

class CashFlowSectionForm(forms.ModelForm):
    class Meta:
        model = CashFlowSection
        fields = ['name']
        widgets = {
            'name': forms.Select(attrs={'class': 'form-select'})
        }

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['section', 'description', 'amount','date']
        widgets = {
            'section': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class CashFlowStatementForm(forms.ModelForm):
    class Meta:
        model = CashFlowStatement
        fields = ['transactions', 'beginning_balance']
        widgets = {
            'transactions': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'beginning_balance': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    # Optionally add these fields if you want to display them as read-only
    change_in_cash = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )
    ending_balance = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )
