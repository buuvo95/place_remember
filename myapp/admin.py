from django.contrib import admin
from django.forms.widgets import TextInput
import json
from .models import Memory

from django_google_maps.widgets import GoogleMapsAddressWidget
from django_google_maps.fields import AddressField, GeoLocationField


class ModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        AddressField: {
            'widget': GoogleMapsAddressWidget(attrs={
                    'data-autocomplete-options': json.dumps({ 'types': ['geocode','establishment'], 'componentRestrictions': {'country': 'us'}})
                }
            )
        },
        GeoLocationField: {
            'widget': TextInput(attrs={
                'readonly': 'readonly'
            })
        },
    }

admin.site.register(Memory, ModelAdmin)