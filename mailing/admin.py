from django.contrib import admin

from mailing.models import Client, Mailing, Message, Log


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name', 'comment', )
    list_filter = ('email', 'full_name',)
    search_fields = ('email', 'full_name',)


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('start_time', 'frequency', 'status', 'recipient')
    list_filter = ('start_time', 'frequency', 'status',)
    search_fields = ('name', 'description',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('mailing', 'subject', 'body', )
    list_filter = ('subject', 'body',)
    search_fields = ('subject', 'body',)


@admin.register(Log)
class LogAdmin(admin.ModelAdmin):
    list_display = ('stamp_time', 'status', 'response', )
    list_filter = ('status', 'response',)
    search_fields = ('status', 'response',)
