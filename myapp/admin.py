from django.contrib import admin
from myapp.models import Bbs

# Register your models here.
class BbsAdmin(admin.ModelAdmin):
    list_display = ('title','author','created',)

admin.site.register(Bbs,BbsAdmin)