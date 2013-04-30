from django.contrib import admin
from django import forms

from .widgets import AddressWithMapWidget

class AddressForm(forms.ModelForm):
    class Meta:
        widgets = {
            'address': AddressWithMapWidget({'class': 'vTextField'})
        }

    class Media:
        js = (
            'https://maps.google.com/maps/api/js?sensor=false',
            'js/easy_maps.js',
        )

class AddressAdmin(admin.ModelAdmin):
    list_display = ['address', 'computed_address', 'latitude', 'longitude', 'geocode_error']
    list_filter = ['geocode_error']
    search_fields = ['address']

    form = AddressForm

class AddressInlineAdmin(admin.StackedInline):
    form = AddressForm
