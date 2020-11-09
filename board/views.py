from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'index.html')
    # return HttpResponse('Hello, Django Board')


def list(request):
    return render(request, 'board/list.html')


def view(request):
    return render(request, 'board/view.html')


def write(request):
    return render(request, 'board/write.html')


def update(request):
    return render(request, 'board/update.html')


def delete(request):
    return render(request, 'board/delete.html')
