from django.contrib import admin
from .models import UserDetails,Transaction,oldTransaction
# Register your models here.
admin.site.register(UserDetails)
admin.site.register(Transaction)
admin.site.register(oldTransaction)
