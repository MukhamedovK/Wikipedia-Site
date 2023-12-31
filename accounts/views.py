from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout, authenticate


def register(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password')
        password2 = request.POST.get('password1')
        if not username.isdigit():
            if not User.objects.filter(username=username).exists():
                if password1 == password2:
                    user = User.objects.create_user(
                        username=username, password=password1
                    )
                    login(request, user)
                    return redirect("home")
                else:
                    context['error'] = "Parol bir xil bo`lishi kerak!"
            else:
                context['error'] = "Bunday username mavjud!"
        else:
            context['error'] = "Username raqamdan iborat bo`lolmaydi!"
    return render(request, 'accounts/register.html', context=context)


def log_in(request):
    context = {}
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            context['error'] = "Username yoki parol xato!"

    return render(request, "accounts/login.html", context=context)


def logout_page(request):
    logout(request)
    return redirect("login")

