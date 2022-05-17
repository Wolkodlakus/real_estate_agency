from django.contrib import admin

from .models import Flat
from property.models import Complain


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address')
    readonly_fields = ['created_at']
    list_display = (
        'address', 'price', 'new_building', 'construction_year',
        'town', 'owners_phonenumber', 'owner_pure_phone')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)

admin.site.register(Flat, FlatAdmin)

class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display=('user', 'flat', 'text_complain')


admin.site.register(Complain, ComplainAdmin)