from django.shortcuts import render
from django.views.generic import DetailView
from .forms import ProductFilterForm

from django.core.paginator import Paginator

from django.http import JsonResponse


# Create your views here.
from .models import Product, Category, Type, Tag


class CategoryTypeTag: 
    def get_category(self):
        return Category.objects.all()
    
    def get_type(self):
        return Type.objects.all()
    
    def get_tag(self):
        return Tag.objects.all()
    
    def get_product(self):
        return Product.objects.all()
    
    def get_product_type(self):
        return Product.objects.all()



class productionDetailView(CategoryTypeTag,DetailView):
    model = Product
    template_name = 'production/details_view.html'
    context_object_name = 'product'
    slug_field = "url"

def products_list(request):
    products = Product.objects.all()
    form = ProductFilterForm(request.GET)
    if form.is_valid():
        type = form.cleaned_data.get('type')
        category = form.cleaned_data.get('category')
        if type:
            products = products.filter(idtype=type)
        if category:
            products = products.filter(idcategory=category)
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page', 10) 
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'form': form,
    }
    return render(request, 'production/production_home.html', context)

def load_types(request):
    category_id = request.GET.get('category')
    types = Type.objects.filter(products__idcategory=category_id).order_by('title').distinct()
    return JsonResponse(list(types.values('id', 'title')), safe=False)

""" model = Product
    template_name = 'production/production_home.html'
    queryset = Product.objects.all()

class FilterProduction(CategoryTypeTag, ListView):
    template_name = 'production/production_home.html'

    def get_queryset(self):
        queryset = Product.objects.filter(
                Q(idcategory__in=self.request.GET.getlist("category_select")) &
                Q(idtype__in=self.request.GET.getlist("type_select"))
                  )
        return queryset
"""
"""
def production_home(request):
    
    category = Category.objects.all()
    products = Product.objects.all()

    data = {
        'products_list': products, 
        'category_list': category

    }
    return render(request, 'production/production_home.html', data)
"""

