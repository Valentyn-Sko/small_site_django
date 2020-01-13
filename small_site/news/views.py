from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html', context={'a': 6})


def contact(request):
    return render(request, 'mainApp/contact.html', context={'values': ['Please contact me bla bla', 'Phone number']})
