from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Case
from .forms import CaseForm, SignUpForm

@login_required
def case_list(request):
    cases = Case.objects.all()
    return render(request, 'legal_services/case_list.html', {'cases': cases})

@login_required
def case_create(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm()
    return render(request, 'legal_services/case_form.html', {'form': form})

@login_required
def case_update(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm(instance=case)
    return render(request, 'legal_services/case_form.html', {'form': form})

@login_required
def case_delete(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        case.delete()
        return redirect('case_list')
    return render(request, 'legal_services/case_confirm_delete.html', {'case': case})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('case_list')
    else:
        form = SignUpForm()
    return render(request, 'legal_services/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('case_list')
    else:
        form = AuthenticationForm()
    return render(request, 'legal_services/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')
