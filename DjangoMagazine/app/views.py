"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from app.models import Feature, Product


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    products = Product.objects.all()[::1]
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
            'products':products,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def product(request, id_product):
    """Renders the product page."""
    assert isinstance(request, HttpRequest)
    try:
        title = Product.objects.get(id=id_product)
    except Product.DoesNotExist:
        raise Http404(f'Product #{id_product} does not exist')

    product_details = Feature.objects.filter(product=title)

    return render(
        request,
        'app/product.html',
        {
        'title':title.name,
        'year':datetime.now().year,
        'details':product_details,
        'id':id
        }
        )