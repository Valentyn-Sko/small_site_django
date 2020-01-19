from django.shortcuts import render

from .models import Product


def products_list(request):
    # posts = search_logic(request)
    # context = paginator_logic(request, posts)
    products = Product.objects.all()

    return render(request, 'sitefurniture/index.html', context={"products": products})
