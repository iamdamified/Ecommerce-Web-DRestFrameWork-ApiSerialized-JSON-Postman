from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Subscriber)
admin.site.register(Social)


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "category", "price"]

admin.site.register(Product, ProductAdmin)


# class ContactAdmin(admin.ModelAdmin):
#     list_display = ["name", "subject", "message"]

# admin.site.register(Contact, ContactAdmin)


# class ContactinfoAdmin(admin.ModelAdmin):
#     list_display = ["name", "email", "message"]

# admin.site.register(Contactinfo, ContactinfoAdmin) # This could be used and the above deleted
