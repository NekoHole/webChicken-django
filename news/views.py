from django.shortcuts import render, redirect
from .models import Articles
from django.views.generic import DetailView

# Create your views here.

class newsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news':news}) #Выводим О нас из другого приложения, а именно main | И передём по ключу news такой объект как news, как определённый Ключ
