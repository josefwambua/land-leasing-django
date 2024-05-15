from django.contrib import admin
from .models import Farmer, Land, Lease

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'user')
    search_fields = ('name', 'user__username')

@admin.register(Land)
class LandAdmin(admin.ModelAdmin):
    list_display = ('location', 'size', 'farmer')
    search_fields = ('location', 'farmer__name')
    list_filter = ('location', 'farmer__name')

@admin.register(Lease)
class LeaseAdmin(admin.ModelAdmin):
    list_display = ('land', 'lessee', 'start_date', 'end_date', 'farmer_approved', 'lessee_approved')
    search_fields = ('land__location', 'lessee__username')
    list_filter = ('start_date', 'end_date', 'farmer_approved', 'lessee_approved')
    actions = ['approve_lease', 'reject_lease']

    def approve_lease(self, request, queryset):
        queryset.update(farmer_approved=True, lessee_approved=True)
        self.message_user(request, "Selected leases have been approved.")
    approve_lease.short_description = "Approve selected leases"

    def reject_lease(self, request, queryset):
        queryset.update(farmer_approved=False, lessee_approved=False)
        self.message_user(request, "Selected leases have been rejected.")
    reject_lease.short_description = "Reject selected leases"

    