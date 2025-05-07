from django.db import models

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=30) 
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    social_media = models.CharField(max_length=30)

    def __str__(self):
        return f"Customer: {self.id}, Name: {self.name}"


class Interaction(models.Model):
    CHANNEL_CHOICES = [
        ('phone', 'Phone'),
        ('sms', 'SMS'),
        ('email', 'Email'),
        ('letter', 'Letter'),
        ('social_media', 'Social Media'),
    ]

    DIRECTION_CHOICES = [
        ('inbound', 'Inbound'),
        ('outbound', 'Outbound'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) #One-To-Many Relationship
    channel = models.CharField(max_length=15, choices=CHANNEL_CHOICES)
    direction = models.CharField(max_length=10, choices=DIRECTION_CHOICES)
    interaction_date = models.DateField(auto_now_add=True)
    summary = models.TextField()