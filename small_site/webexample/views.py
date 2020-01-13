from django.http import HttpResponse


def index(request):
    return HttpResponse("<h3>Hello world</h3>")
