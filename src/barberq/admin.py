from barberq.models import Barber, Client, Reservation, Service, User
from django.contrib import admin

admin.site.register(User, admin.ModelAdmin)
admin.site.register(Barber, admin.ModelAdmin)
admin.site.register(Client, admin.ModelAdmin)
admin.site.register(Reservation, admin.ModelAdmin)
admin.site.register(Service, admin.ModelAdmin)
