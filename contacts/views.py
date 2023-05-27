from django.shortcuts import render, redirect
from .forms import ContaForm

# Create your views here.
def contacts(request): 
    return render(request, 'contacts/contacts.html')

def create(request):
    error = '' #Да, так вот строковая переменная создаётся в питоне
    if request.method == 'POST': #ебать какое сложно объеснение было, но типа потому что <form method="post">
        form = ContaForm(request.POST) #Здесь будт находить объект со всеми данными из формы от пользоватея 
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