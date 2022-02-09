# Standard library imports
from django.contrib import admin

# Related third party imports

# Local application/library specific imports
from .models import Message

# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ['conversation_id', 'message_text']
    
    list_per_page = 25


admin.site.register(Message, MessageAdmin)