# coding=utf-8
from django.db import models
from django.utils import timezone
# from django.template.defaultfilters import truncatechars
# import PIL as pillow

class status(models.Model):
    name = models.CharField(max_length=128, blank=True, null=True, default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Статус тикета'
        verbose_name_plural = 'Статусы тикетов'

class Ticket(models.Model):

    name = models.CharField(max_length=128, blank=True, null=True, default=True)
    status = models.ForeignKey(status, blank=True, null=True, default=True, on_delete=models.CASCADE)
    surname = models.CharField(max_length=128, blank=True, null=True, default=True)
    town = models.CharField(max_length=32, blank=True, null=True, default=True)
    phone = models.CharField(max_length=68, blank=True, null=True, default=True)
    message = models.TextField(blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    # status = models.ForeignKey(status, on_delete=models.CASCADE)
    # ticket_type = models.ForeignKey(ticket_type, default=True, on_delete=models.CASCADE)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)
    is_main = models.BooleanField(default=False)
    chat_id = models.CharField(max_length=20, blank=True, null=True, default=None)
    chat_messages = models.TextField(default="", null=True, blank=True)

    class Meta:
        verbose_name = 'Тикет'
        verbose_name_plural = 'Тикеты'

# class TicketCategory(models.Model):
#     Ticket = models.ForeignKey(Ticket, blank=True, null=True, default=None, on_delete=models.CASCADE)
#     # image = models.ImageField(upload_to='products_images/')
#     # name = models.CharField(max_length=128, blank=True, null=True, default=True)
#     status = models.ForeignKey(status, blank=True, null=True, default=True, on_delete=models.CASCADE)
#     is_main = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     created = models.DateTimeField(default=timezone.now)
#     updated = models.DateTimeField(default=timezone.now)
#
#     def __str__(self):
#             return "%s" % (self.id)
#
#     class Meta:
#         verbose_name = 'Информация о тикете'
#         verbose_name_plural = 'Информация о тикетах'
