from django import forms

from .models import Room, Building


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['room_id']


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        exclude = ['building_id']
