from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Service, ContactMessage


def index(request):
    services = Service.objects.all()
    return render(request, 'index.html', {'services': services})


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        company = request.POST.get('company')
        message = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            company=company,
            message=message,
        )

        messages.success(request, f"Thanks {name}, we'll be in touch shortly!")
        return redirect('contact')

    return render(request, 'contact.html')


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)
    other_services = Service.objects.exclude(slug=slug)

    return render(request, 'service_detail.html', {
        'service': service,
        'other_services': other_services,
    })