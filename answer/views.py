from django.shortcuts import render
from .models import Answer
# Create your views here.
def answer(request):
    answers = Answer.objects.all()
    context = {
        'answerr_out': answers
    }
    return render(request, 'answer/answer.html', context)