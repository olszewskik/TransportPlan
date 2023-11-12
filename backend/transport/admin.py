from django.contrib import admin
from .models import Transport, Company, Customer, Vendor, Address, Carrier


class CarrierAdmin(admin.ModelAdmin):
    list_display = ("name", "phone_no", "email")


class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("name",)


class VendorAdmin(admin.ModelAdmin):
    list_display = ("name",)


class TransportAdmin(admin.ModelAdmin):
    list_display = ("status", "transport_type", "date", "time", "carrier")


class AddressAdmin(admin.ModelAdmin):
    list_display = ("street", "city", "postal_code", "country")


admin.site.register(Transport, TransportAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Carrier, CarrierAdmin)
