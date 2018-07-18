from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from django.shortcuts import render
from products.models import *
# from utils.uploadings import UploadingProducts
# from django.contrib import messages
from django.http import HttpResponseRedirect

from telegram.ext import Updater, Filters, MessageHandler, dispatcher
import telegram




def product(request, product_id):
    products = Ticket.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    message = products.chat_messages.split("\n")
    time=products.created
    print(time)
    messages=""#str(mesgsage)

    i = -1
    for t in message:
        if "user" in t:
            messages += products.name+" "+products.surname+t[4: ]+"\n"+time.strftime("%d.%m.%Y %H:%M:%S")+"\n"
        elif "admin" in t:
            messages +=t+"\n"+time.strftime("%d.%m.%Y %H:%M:%S")+"\n"
        else:
            i -= 1

    return render(request, 'products/product.html', locals())

def send_message(request, product_id):
    products = Ticket.objects.get(id=product_id)
    chat_id = products.chat_id
    b = products.chat_messages + "admin: " + request.POST["msg"] + "\n"
    Ticket.objects.filter(chat_id=chat_id).update(chat_messages=b)
    print(products.chat_messages)
    print(request.POST)

    token = "631227260:AAGmtcTJgc25d37m4OGwPVIyImeJeDmbmIU"
    bot = telegram.Bot(token)
    bot.send_message(chat_id=chat_id, text=request.POST["msg"])

    Ticket.objects.filter(pk=product_id).update(status_id=2)
    products.refresh_from_db()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
    # return render(request, 'landing/home.html', locals())

def add_to_close(request, product_id):
    products = Ticket.objects.get(id=product_id)
    Ticket.objects.filter(pk=product_id).update(status_id=4)
    products.refresh_from_db()

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
