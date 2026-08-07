
from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_objets = Phone.objects.all()
    phones = [p for p in phones_objets]
    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones_objets = phones_objets.order_by('name')
    elif sort == 'min_price':
        phones_objets = phones_objets.order_by('price')
    elif sort == 'max_price':
        phones_objets = phones_objets.order_by('-price')

    context = {
        'phones':phones_objets,
        'sort': sort,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {
        'phone':phone,
    }
    return render(request, template, context)
