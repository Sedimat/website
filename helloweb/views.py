from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random

# Create your views here.
def index(request):
    number = 100
    return HttpResponse(f"""
    <center><h1>Голована сторінка, сама перша</h1></center>
    <center><h2>{number}</h2></center>
    <center><a href="index2">Головна</a></center>
    <center><a href="django">Джанго</a></center>
    <center><a href="date">Дата</a></center>
    <center><a href="rand">Рандомна</a></center>
    <center><a href="news">Новини</a></center>
    <center><a href="management">Менеджмент</a></center>
    <center><a href="history">Історія</a></center>
    
    """)


def index2(request):
    number = 100
    return HttpResponse(f"""
    <center><h1>Голована сторінка, сама перша</h1></center>
    <center><h2>{number}</h2></center>
    <center><a href="index2">Головна</a></center>
    <center><a href="django">Джанго</a></center>
    <center><a href="date">Дата</a></center>
    <center><a href="rand">Рандомна</a></center>
    <center><a href="news">Новини</a></center>
    <center><a href="management">Менеджмент</a></center>
    <center><a href="history">Історія</a></center>

    """)

def history(request):
    number1 = "test"
    return HttpResponse(f"""
        <center><h1>Тут знаходиться історія вашого міста: Сміла</h1></center>
        <center><h2>Сміла та її околиці були заселені ще здавна, про що свідчать залишки давніх поселень та численних курганів,
        виявлених у різних частинах міста та поблизу нього.
        Два значних древніх городища та 44 кургани вперше були досліджені у 1879—1883 роках О. О.
        Бобринським, онуком власника Сміли графа Олексія Олексійовича Бобринського.
        Ці знахідки датуються приналежністю частково до кам'яної доби, частково до бронзової.
        Офіційна дата народження Сміли 1542 рік. У XVI столітті в документах Великого князівства Литовського зазначено що на місці хутора
        в 1542 році з'являється поселення Яцькове-Тясмино. Назва Сміла відома з першої половини 17 століття. Із назвою міста пов'язана легенда,
        яку записав граф Л. О. Бобринський: «Якась-то дівчина провела воїнів через важкодоступне болото в тил до ворога.
        Вони перемогли тьму-тьмущу ворогів у кривавій битві, але дівчину не вберегли.
        Поховали воїни героїню над Тясмином і назвали її Смілою, а містечко Тясмин на її честь назвали Смілою»</h2></center>
        <center><img id="img1" src="https://zno.org.ua/wp-content/uploads/2018/09/hist2.png"></center>
        <center><a href="index2">Головна</a></center>
        <center><a href="history/photos">Photo</a></center>
        <center><a href="history/people">People</a></center>
        """)

def photos(request):
    return HttpResponse(f"""
            <center><h1>Тут знаходиться фотографії вашого міста</h1></center>
            <center><a href="/index2">Головна</a></center>
            <center><a href="/history">Назад до Історія</a></center>
            <center><h1>Покровська церква біля річки Тясмин</h1></center>
            <center><img id="img1" src="https://lh6.ggpht.com/_Mh4TiRyzl18/S6iSHT_YlmI/AAAAAAAABTo/L4xZJRtYZzg/s0/9424_.jpg"></center>
            """)

def people(request):
    return HttpResponse(f"""
            <center><h1>Тут знаходиться інформація відомих жителів</h1></center>
            <center><a href="/index2">Головна</a></center>
            <center><a href="/history">Назад до Історія</a></center>
            <center><h2>Мер міста сміла Сергій Ананко</h2></center>
            <center><img id="img1" src="https://argumentua.com/i/6666--203-1-2393902-2-20-2023.png"></center>
            """)



def django(request):
    number1 = 200
    return HttpResponse(f"""
    <h1>Hello from django v2 </h1>
    <h2>{number1}</h2>
    <center><a href="index2">Головна</a></center>
    """)

def date(request):
    day_of_week_text = {
        0: "понеділок",
        1: "вівторок",
        2: "середа",
        3: "четвер",
        4: "п'ятниця",
        5: "субота",
        6: "неділя",
    }
    today = datetime.datetime.now()
    day_of_week = today.weekday()

    return HttpResponse(f"""
    <h1>Зараз {today}</h1>
    <h2>Сьогоднішній день: {day_of_week_text[day_of_week]}</h2>
    <center><a href="index2">Головна</a></center>
    """)

def random_frase(request):
    dict1 = [
        "Велика неділя",
        "Завтра буде зватра",
        "its wednesday my dudes",
        "Увага Анекдот",
        "Завтра ніколи не настає, завжди сьогодні"
    ]
    randomF = random.choice(dict1)
    return HttpResponse(f"""
    <h1>Рондомна фраза з списку</h1>
    <h2>Сьогоднішній день: {randomF}</h2>
    <center><a href="index2">Головна</a></center>
    """)

def news(request):
    return HttpResponse(f"""
    <center><h1>Тут знаходиться дуже важливі новини!!</h1></center>
    <center><a href="index2">Головна</a></center>
    """)

def management(request):
    return HttpResponse(f"""
    <center><h1>Це сторінка менеджменту</h1></center>
    <center><a href="index2">Головна</a></center>
    """)