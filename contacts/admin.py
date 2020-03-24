from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','user_id','listing','email','contact_date')
    list_display_link = ('name','id','email')
    list_filter = ('contact_date',)
    search_fields = ('name','email','listing')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)
