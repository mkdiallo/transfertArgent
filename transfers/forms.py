from django import forms
from .models import Client, Transfer

class SenderClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'country', 'city']

class RecipientClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number', 'country', 'city']

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ['sender', 'recipient', 'amount']
