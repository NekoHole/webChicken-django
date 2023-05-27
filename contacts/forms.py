from .models import ContactForm
from django.forms import ModelForm, TextInput, Textarea, Select

class ContaForm(ModelForm):  #Класс, название любое, но обычно __НазваниеForm__(от чего наследуем)
    class Meta: # Вложенный класс должен называться Meta
        model = ContactForm 
        fields = ['name', 'full_text', 'idcategory', 'email', 'phoneNumber' ]
        
        #Выглядить должно по итогу как  <input type="text" placeholder="Название статьи" class="form-control"><br>
        widgets = { # Словарь характеристик для полей??????
            "name": TextInput(attrs={ #Так, Ну... В класс TextInpu мы передаём атрибуты в виде словаря, ок?
                'class': 'form-control',
                'placeholder': 'ФИО'
            }),
            "full_text": Textarea(attrs={ 
                'class': 'form-control', 
                'placeholder': 'Введите своё предложение или вопрос'
            }), 
            "phoneNumber": TextInput(attrs={ 
                'type' : 'tel',
                'pattern' : '[+]{1}[0-9]{11,15}', 
                'class': 'form-control', 
                'placeholder': 'Введите свой номер телефона'
            }),
            "email": TextInput(attrs={ 
                'type' : 'email', 
                'class': 'form-control', 
                'placeholder': 'Введите email'
            }),
            "idcategory": Select(attrs ={
                'class': 'form-control', 
                'placeholder': 'выбор'
            })
        }