from django.contrib import admin
from myapp.models import *
# Register your models here.
admin.site.register(User)
admin.site.register(emailverification)
admin.site.register(Ticket)
admin.site.register(Contact)
