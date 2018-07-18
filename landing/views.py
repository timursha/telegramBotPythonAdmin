from django.shortcuts import render
from products.models import *

# def home(request):
#
#     status_container = status.objects.filter(is_active=True, ticket__is_active=True)
#     status_container_1 = status_container.filter(ticket__status__id=1)
#     status_container_2 = status_container.filter(ticket__status__id=2)
#     status_container_3 = status_container.filter(ticket__status__id=3)
#     status_container_4 = status_container.filter(ticket__status__id=4)
#
#     return render(request, 'landing/home.html', locals())

# def messages (request):
#
#     products_images = TicketImage.objects.filter(is_active=True, is_main=True, Product__is_active=True)
#     products_images_1 = products_images.filter(Product__category__id=1)
#     products_images_2 = products_images.filter(Product__category__id=2)
#
#     return render(request, 'products/messages.html', locals())

def landing(request):
    return render(request, 'landing/landing.html', locals())

def home(request):
    ticket_categories = Ticket.objects.filter(is_active=True)
    ticket_categories_1 = ticket_categories.filter(status=1)
    ticket_categories_2 = ticket_categories.filter(status=2)
    ticket_categories_3 = ticket_categories.filter(status=3)
    ticket_categories_4 = ticket_categories.filter(status=4)

    # all_records =

    return render(request, 'landing/home.html', locals())

# def home(request):
#     products_images = TicketImage.objects.filter(is_active=True, is_main=True, Ticket__is_active=True)
#     products_images_1 = products_images.filter(Ticket__status__id=1)
#     products_images_2 = products_images.filter(Ticket__status__id=2)
#     products_images_3 = products_images.filter(Ticket__status__id=3)
#     products_images_4 = products_images.filter(Ticket__status__id=4)
#     return render(request, 'landing/home.html', locals())

