from django.shortcuts import render
from production.models import Product

# Create your views here.
def main(request):
    products = Product.objects.all()[:5]
    context = {
        'page_obj': products
    }
    return render(request, 'main/main.html', context)
