from django.shortcuts import render, redirect
from .forms import ContaForm

# Create your views here.
def contacts(request): 
    return render(request, 'contacts/contacts.html')

def create(request):
    error = '' 
    if request.method == 'POST': 
        form = ContaForm(request.POST) 
        if form.is_valid():
            form.save()
            error = 'Корректное'
            return redirect (create)
        else:
            error = 'Форма заполненна не корректно. \n'

     #Создаём объет form названиеЛюбое на основе ArticlesForm()
    form = ContaForm(request.POST or None)

    data = {   #Это словарь создаём, который потом передавать будем 
        'form': form, # 'ключ_названиеЛюбое': объект 
        'error': error
    }

    return render(request, 'contacts/contacts.html', data)