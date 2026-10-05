from django.shortcuts import render, redirect
from django.contrib import messages


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        messages.success(request, f"Thanks {name}, your message has been received!")
        return redirect('contact')

    return render(request, 'contact.html')