import json
from django import forms
from django.db.models import fields
from .models import Memory
from django_google_maps.widgets import GoogleMapsAddressWidget

class MemoryModelForm(forms.ModelForm):
    class Meta(object):
        model = Memory
        fields = [
            'name',
            'address', 
            'geolocation',
            'comment',
        ]
        widgets = {
            "address": GoogleMapsAddressWidget(
                attrs={
                        'data-autocomplete-options': json.dumps({ 'types': ['geocode',
                        'establishment'], 'componentRestrictions': {
                                    'country': 'us'
                                }
                            })
                        }),
        }