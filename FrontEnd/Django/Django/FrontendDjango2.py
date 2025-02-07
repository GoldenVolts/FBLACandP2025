from django.shortcuts import render, get_object_or_404, redirect
from .FrontendDjango import Income, Expense
from .FrontendDjango3 import IncomeForm, ExpenseForm

def home(request):
    incomes = Income.objects.all()
    expenses = Expense.objects.all()
    balance = sum(income.amount for income in incomes) - sum(expense.amount for expense in expenses)
    return render(request, 'finances/home.html', {
        'incomes': incomes,
        'expenses': expenses,
        'balance': balance,
    })

def add_income(request):
    if request.method == 'POST':
        form = IncomeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncomeForm()
    return render(request, 'finances/add_income.html', {'form': form})

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm()
    return render(request, 'finances/add_expense.html', {'form': form})

def edit_income(request, income_id):
    income = get_object_or_404(Income, id=income_id)
    if request.method == 'POST':
        form = IncomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncomeForm(instance=income)
    return render(request, 'finances/edit_income.html', {'form': form})

def edit_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'finances/edit_expense.html', {'form': form})

def delete_income(request, income_id):
    income = get_object_or_404(Income, id=income_id)
    income.delete()
    return redirect('home')

def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)
    expense.delete()
    return redirect('home')