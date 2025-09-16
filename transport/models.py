from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    USER_TYPES = (
        ('customer', 'Naručilac'),
        ('driver', 'Vozač'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='customer')
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    is_premium = models.BooleanField(default=False)  # Za vrhunsku uslugu

    def __str__(self):
        return f"{self.user.username} - {self.get_user_type_display()}"

class Ride(models.Model):
    STATUS_CHOICES = (
        ('requested', 'Zatraženo'),
        ('accepted', 'Prihvaćeno'),
        ('in_progress', 'U toku'),
        ('completed', 'Završeno'),
        ('cancelled', 'Otkazano'),
    )
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rides_as_customer')
    driver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rides_as_driver', null=True, blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='requested')
    pickup = models.CharField(max_length=200)
    dropoff = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Automatski račun za uštedu
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.status == 'completed' and self.driver:
            # Simulacija ekstra zarade: +10% za dopunjene ture
            if self.price:
                self.price += self.price * 0.1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.user.username} -> {self.pickup} to {self.dropoff} ({self.status})"

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
