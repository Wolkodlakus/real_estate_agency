from django.contrib import admin

from .models import Flat
from property.models import Complain, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    verbose_name = 'Владельцы'
    verbose_name_plural = 'Владельцы квартиры'
    raw_id_fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address')
    readonly_fields = ['created_at']
    list_display = (
        'address', 'price', 'new_building',
        'construction_year', 'town')
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('liked_by',)
    inlines = [OwnerInline]


@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display = ('user', 'flat', 'text_complain')


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)
    list_display = ('owner', 'phone', 'pure_phone')
