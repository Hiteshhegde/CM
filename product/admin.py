from django.contrib import admin
from .models import Offer, Location, Redemption


# Register your models here.

class OfferAdmin(admin.ModelAdmin):

    list_display = ('redeem_status', 'sort_title', 'sort_sponsor_name', 'sort_start_time', 'sort_end_time')
    list_filter = ('sponsor_name', 'start_time', 'end_time')
    search_fields = [('title', 'sponsor_name')]


    #@admin.display(ordering='sort_title')
    def sort_title(self, obj):
        return obj.title

    sort_title.admin_order_field = "title"
    sort_title.short_description = "Sort by Title"

    def sort_sponsor_name(self, obj):
        return obj.sponsor_name

    sort_sponsor_name.admin_order_field = "sponsor_name"
    sort_sponsor_name.short_description = "Sort by sponsor name"

    def sort_start_time(self, obj):
        return obj.start_time
    
    sort_start_time.admin_order_field = "start_time"
    sort_start_time.short_description = "Sort by Start time"

    def sort_end_time(self, obj):
        return obj.end_time
    
    sort_end_time.admin_order_field = "end_time"
    sort_end_time.short_description = "Sort by End time"


admin.site.register(Offer, OfferAdmin)
admin.site.register(Location)
admin.site.register(Redemption)
