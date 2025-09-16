from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Ride, Profile

class RegisterForm(UserCreationForm):
    user_type = forms.ChoiceField(choices=Profile.USER_TYPES, widget=forms.RadioSelect)
    phone = forms.CharField(max_length=20, required=False)
    address = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'user_type', 'phone', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            profile = Profile.objects.get(user=user)
            profile.phone = self.cleaned_data['phone']
            profile.address = self.cleaned_data['address']
            profile.save()
        return user

class RideRequestForm(forms.ModelForm):
    class Meta:
        model = Ride
        fields = ('pickup', 'dropoff')
        widgets = {
            'pickup': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa polaska'}),
            'dropoff': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa dolaska'}),
        }
