from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def my_form(request):
    if request.method == 'POST':
        # Отримати дані з форми
        username = request.POST.get('username')
        password = request.POST.get('password')

        context = {
            "user": username,
            "pass": password

        }
        return render(request, 'hw37/my_form.html', context=context)

def index(request):
    context = {
        "test": "Blog test"
    }
    return render(request, 'hw37/index.html', context=context)


def single(request):
    context = {
        "test": "Blog test"
    }
    return render(request, 'hw37/single.html', context=context)

def demo(request):
    context = {
        "test": "Blog test"
    }
    return render(request, 'hw37/demo.html', context=context)

def page(request):
    context = {
        "test": "Blog test"
    }
    return render(request, 'hw37/page.html', context=context)

def blog(request):
    context = {
        "test": "Blog test"
    }
    return render(request, 'hw37/blog.html', context=context)

def archives(request):
    context = {
        "test": "Blog test"
    }
    return render(request, 'hw37/archives.html', context=context)