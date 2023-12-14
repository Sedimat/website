from django.shortcuts import render

# Create your views here.
def showInt():
    return 123

def index(request):
    title = "Python DTL"
    list1 = ['one','two','three']
    context = {
        'title': title,
        'now': "09.11.23",
        'number': showInt,
        'list_data': list1
    }
    return render(request,'testWork/index.html',context=context)

def contact(request):
    title = "Контакти"
    context = {
        'title': title,
        'now': "09.11.23",
        'number': showInt,
        'contact': "Наші контакти +380780678671"
    }
    return render(request, 'testWork/contact.html', context=context)

def info(request):
    title = "Інформація"
    context = {
        'title': title,
        'now': "Інформація про наш магазин",
        'info': "На цьому сайті у нас можна оформити та замовити конверти та відкритки",
        't1': "We are the champions, my friends And we'll keep on fighting till the end Queen, We are the champions"
    }
    return render(request, 'testWork/info.html', context=context)

def hw1(request):
    context = {
        't1': "We are the champions, my friends And we'll keep on fighting till the end Queen, We are the champions"
    }
    return render(request, 'testWork/hw1.html', context=context)
