from django.shortcuts import render

# Create your views here.
def career(request):
    return render(request, 'career/career.html')