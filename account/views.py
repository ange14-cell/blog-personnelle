from django.contrib.auth import login
from django.shortcuts import render, redirect
from account.forms import SignupForm


def signup(request):
    context = {}
    if request.method =='POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post:home')
        else:
            context["errors"] = form.errors
    form = SignupForm()
    context["form"] = form
    return render(request, 'account/signup.html', context=context)
