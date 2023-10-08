from django.db import models
import random
import string

def generate_unique_code():
    length = 10
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if not Transfer.objects.filter(code=code).exists():
            return code

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Transfer(models.Model):
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sent_transfers')
    recipient = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='received_transfers')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.CharField(max_length=10, unique=True, default=generate_unique_code)

    def __str__(self):
        return f"Transfer #{self.id} - {self.sender.first_name} to {self.recipient.first_name}"

