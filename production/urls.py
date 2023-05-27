from django.urls import path
from . import views


urlpatterns = [
    path('', views.products_list, name='production_home'),
    path('ajax/load-types/', views.load_types, name='ajax_load_types'), # AJAX
    path('<slug:slug>', views.productionDetailView.as_view(), name='production_detail')
]