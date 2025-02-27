from django.shortcuts import render
import datetime

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is my first page</h1>")

def date_time(request):
    date = datetime.datetime.now()
    h = int(date.strftime("%H"))
    m = int(date.strftime("%M"))
    s = int(date.strftime("%S"))

    if h < 12:
        msg = "Rise up, start fresh, and see the bright opportunity in every day. Good Morning!"
    elif h < 16:
        msg = "Make each afternoon a masterpiece by filling it with productivity and joy."
    elif h < 21:
        msg = "Evenings are life's way of saying, you've survived the day—now relax and recharge."
    else:
        msg = "The night is a reminder that dreams are just within reach if you dare to sleep and believe."

    my_dict = {
        'date': date,
        'msg': msg,
        'hour_deg': (h % 12) * 30 + m * 0.5,  
        'minute_deg': m * 6, 
        'second_deg': s * 6  
    }

    return render(request, 'accounts/home.html', my_dict)
