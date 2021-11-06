from .models import Reservation
from django.forms import ModelForm, TextInput, Textarea


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["name", "seat", "phone_number", "quantity_of_people", "date", "time", "note"]
        widgets = {
            "name": TextInput(attrs={
                'id': 'name',
                'placeholder': 'Ім`я',
                'name': 'name',
                'type': 'text'
            }),
            "seat": TextInput(attrs={
                'id': 'seat',
                'placeholder': 'Місце',
                'name': 'name',
                'type': 'text'
            }),
            "phone_number": TextInput(attrs={
                'id': 'phone',
                'placeholder': 'Номер телефону',
                'name': 'phone',
                'type': 'text'
            }),
            "quantity_of_people": TextInput(attrs={
                'id': 'seats',
                'placeholder': 'К-сть людей',
                'name': 'seats',
                'type': 'text'
            }),
            "date": TextInput(attrs={
                'id': 'date',
                'placeholder': 'Дата',
                'name': 'date',
                'type': 'date'
            }),
            "time": TextInput(attrs={
                'id': 'time',
                'placeholder': 'Час',
                'name': 'time',
                'type': 'time'
            }),
            "note": Textarea(attrs={
                'id': 'requests',
                'placeholder': 'Примітка',
                'name': 'requests',
                'rows': '4'
            })
        }
