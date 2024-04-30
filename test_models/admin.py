from django.contrib import admin
from .models import Person, Article, Publication, MySpecialUser
# Register your models here.
admin.site.register(Person)
admin.site.register(Article)
admin.site.register(Publication)
admin.site.register(MySpecialUser)