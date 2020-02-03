from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Product, TypeFurniture


def products_list(request):
    # posts = search_logic(request)
    # context = paginator_logic(request, posts)
    products = Product.objects.all()

    return render(request, 'sitefurniture/index.html', context={"products": products})


class TypeDetail(View):
    # posts = search_logic(request)
    # context = paginator_logic(request, posts)
    model = TypeFurniture

    def get(self, request, slug):
        print(slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        # return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj, 'detail': True})
        print(obj)
        return render(request, 'sitefurniture/type_detail.html', context={"typeF": obj})


def types_list(request):
    types = TypeFurniture.objects.all()

    return render(request, 'sitefurniture/types.html', context={"types": types})


class ProductDetail(View):
    model = Product
    template = 'sitefurniture/item.html'

    def get(self, request, slug):
        print(slug)
        obj = get_object_or_404(self.model, slug__iexact=slug)
        # return render(request, self.template, context={self.model.__name__.lower(): obj, 'admin_object': obj, 'detail': True})
        print(obj)
        return render(request, 'sitefurniture/item.html', context={'item': obj})
