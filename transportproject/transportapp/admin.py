from django.contrib import admin

# Register your models here.
from .models import Questions
from .models import  Answers
from .models import  Likes

admin.site.register(Questions)
admin.site.register(Answers)
admin.site.register(Likes)