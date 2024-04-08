from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def add_to_list(request):
    pass

# Create your views here.
