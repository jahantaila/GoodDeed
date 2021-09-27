from django.contrib import admin
from home.models import Donation, Request, UserDetail, Contact
# Register your models here.

admin.site.register(Donation)
admin.site.register(UserDetail)
admin.site.register(Contact)
admin.site.register(Request)


