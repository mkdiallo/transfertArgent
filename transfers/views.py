from django.shortcuts import render, redirect
from django.views import View
from .forms import SenderClientForm, RecipientClientForm, TransferForm
from .models import Client, Transfer

class SenderClientCreateView(View):
    template_name = 'transfers/sender_client_form.html'

    def get(self, request):
        form = SenderClientForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SenderClientForm(request.POST)
        if form.is_valid():
            sender_client = form.save()
            return redirect('transfers:recipient_client_create', sender_client.id)  # Rediriger vers la création du client bénéficiaire
        return render(request, self.template_name, {'form': form})

class RecipientClientCreateView(View):
    template_name = 'transfers/recipient_client_form.html'

    def get(self, request, sender_client_id):
        sender_client = Client.objects.get(id=sender_client_id)
        form = RecipientClientForm()
        return render(request, self.template_name, {'form': form, 'sender_client': sender_client})

    def post(self, request, sender_client_id):
        sender_client = Client.objects.get(id=sender_client_id)
        form = RecipientClientForm(request.POST)
        if form.is_valid():
            recipient_client = form.save()
            return redirect('transfers:transfer_create', sender_client.id, recipient_client.id)  # Rediriger vers la création du transfert
        return render(request, self.template_name, {'form': form, 'sender_client': sender_client})

class TransferCreateView(View):
    template_name = 'transfers/transfer_form.html'

    def get(self, request, sender_client_id, recipient_client_id):
        sender_client = Client.objects.get(id=sender_client_id)
        recipient_client = Client.objects.get(id=recipient_client_id)
        form = TransferForm()
        return render(request, self.template_name, {'form': form, 'sender_client': sender_client, 'recipient_client': recipient_client})

    def post(self, request, sender_client_id, recipient_client_id):
        sender_client = Client.objects.get(id=sender_client_id)
        recipient_client = Client.objects.get(id=recipient_client_id)
        form = TransferForm(request.POST)
        if form.is_valid():
            form.instance.sender = sender_client
            form.instance.recipient = recipient_client
            form.save()
            return redirect('transfer_list')  # Rediriger vers la liste des transferts
        return render(request, self.template_name, {'form': form, 'sender_client': sender_client, 'recipient_client': recipient_client})


class ClientListView(View):
    template_name = 'transfers/client_list.html'

    def get(self, request):
        clients = Client.objects.all()
        return render(request, self.template_name, {'clients': clients})

class TransferListView(View):
    template_name = 'transfers/transfer_list.html'

    def get(self, request):
        transfers = Transfer.objects.all()
        return render(request, self.template_name, {'transfers': transfers})