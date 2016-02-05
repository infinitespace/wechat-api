from django.contrib import admin

# Register your models here.
from .models import User_text
from .models import User_voice
admin.site.register(User_text)
admin.site.register(User_voice)