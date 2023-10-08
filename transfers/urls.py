from django.urls import path
from . import views

app_name = 'transfers'

urlpatterns = [
    # Vue pour enregistrer le client émetteur
    path('create/sender/', views.SenderClientCreateView.as_view(), name='sender_client_create'),

    # Vue pour enregistrer le client bénéficiaire
    path('create/recipient/<int:sender_client_id>/', views.RecipientClientCreateView.as_view(), name='recipient_client_create'),

    # Vue pour créer un transfert
    path('create/transfer/<int:sender_client_id>/<int:recipient_client_id>/', views.TransferCreateView.as_view(), name='transfer_create'),

    # Vous pouvez également ajouter des vues pour afficher la liste des clients, la liste des transferts, etc.
    # Vue pour afficher la liste des clients
    path('clients/', views.ClientListView.as_view(), name='client_list'),

    # Vue pour afficher la liste des transferts
    path('transfers/', views.TransferListView.as_view(), name='transfer_list'),
]
