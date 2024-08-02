from django.shortcuts import render, get_object_or_404, redirect
from .models import CashFlowSection, Transaction, CashFlowStatement
from .forms import CashFlowSectionForm, TransactionForm, CashFlowStatementForm

# CashFlowSection Views
def index(request):
    context = {
        'title': 'Dashboard'
    }
    return render(request, 'pages/index.html', context)


def section_list(request):
    sections = CashFlowSection.objects.all()
    context = {
        'sections': sections,
        'title': 'Cash Flow Sections'
    }
    return render(request, 'pages/section_list.html', context)

def section_create(request):
    if request.method == 'POST':
        form = CashFlowSectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = CashFlowSectionForm()
    context = {
        'form': form,
        'title': 'Create Cash Flow Section'
    }
    return render(request, 'pages/section_form.html', context)

def section_update(request, pk):
    section = get_object_or_404(CashFlowSection, pk=pk)
    if request.method == 'POST':
        form = CashFlowSectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('section_list')
    else:
        form = CashFlowSectionForm(instance=section)
    context = {
        'form': form,
        'title': 'Update Cash Flow Section'
    }
    return render(request, 'pages/section_form.html', context)

def section_delete(request, pk):
    section = get_object_or_404(CashFlowSection, pk=pk)
    if request.method == 'POST':
        section.delete()
        return redirect('section_list')
    context = {
        'section': section,
        'title': 'Delete Cash Flow Section'
    }
    return render(request, 'pages/section_confirm_delete.html', context)

# Transaction Views
def transaction_list(request):
    transactions = Transaction.objects.all()
    context = {
        'transactions': transactions,
        'title': 'Transactions'
    }
    return render(request, 'pages/transaction_list.html', context)

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    context = {
        'form': form,
        'title': 'Create Transaction'
    }
    return render(request, 'pages/transaction_form.html', context)

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    context = {
        'form': form,
        'title': 'Update Transaction'
    }
    return render(request, 'pages/transaction_form.html', context)

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    context = {
        'transaction': transaction,
        'title': 'Delete Transaction'
    }
    return render(request, 'pages/transaction_confirm_delete.html', context)

# CashFlowStatement Views
def statement_list(request):
    statements = CashFlowStatement.objects.all()
    context = {
        'statements': statements,
        'title': 'Cash Flow Statements'
    }
    return render(request, 'pages/statement_list.html', context)

def statement_create(request):
    if request.method == 'POST':
        form = CashFlowStatementForm(request.POST)
        if form.is_valid():
            statement = form.save(commit=False)
            statement.change_in_cash = sum(transaction.amount for transaction in form.cleaned_data['transactions'])
            statement.ending_balance = statement.beginning_balance + statement.change_in_cash
            statement.save()
            form.save_m2m()  # Save the many-to-many relationships
            return redirect('statement_list')
    else:
        form = CashFlowStatementForm()
    context = {
        'form': form,
        'title': 'Create Cash Flow Statement'
    }
    return render(request, 'pages/statement_form.html', context)


def statement_detail(request, pk):
    statement = get_object_or_404(CashFlowStatement, pk=pk)
    context = {
        'statement': statement,
        'title': 'Cash Flow Statement Detail'
    }
    return render(request, 'pages/statement_detail.html', context)


def statement_delete(request, pk):
    statement = get_object_or_404(CashFlowStatement, pk=pk)
    if request.method == 'POST':
        statement.delete()
        return redirect('statement_list')
    context = {
        'statement': statement,
        'title': 'Delete Cash Flow Statement'
    }
    return render(request, 'pages/statement_confirm_delete.html', context)