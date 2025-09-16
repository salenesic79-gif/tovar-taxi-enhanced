from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, RideRequestForm
from .models import Profile, Ride

def home(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.get(user=user)
            profile.user_type = form.cleaned_data['user_type']
            profile.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    profile = request.user.profile
    if profile.user_type == 'customer':
        rides = Ride.objects.filter(customer=profile)
        # Simulacija uštede: prikaži procenat
        total_savings = sum(ride.price * 0.3 for ride in rides if ride.status == 'completed') if rides else 0
        context = {'rides': rides, 'savings': total_savings, 'user_type': 'customer'}
    else:  # driver
        available_rides = Ride.objects.filter(status='requested', driver__isnull=True)
        # Predlozi za dopunjavanje tura
        earnings = sum(ride.price for ride in profile.rides_as_driver.filter(status='completed')) if profile.rides_as_driver.exists() else 0
        context = {'available_rides': available_rides, 'earnings': earnings, 'user_type': 'driver'}
    return render(request, 'dashboard.html', context)

@login_required
def request_ride(request):
    if request.user.profile.user_type != 'customer':
        return redirect('dashboard')
    if request.method == 'POST':
        form = RideRequestForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            ride.customer = request.user.profile
            ride.save()
            # Simulacija cene sa uštedom
            ride.price = 10.0  # Primer, integrisati mapu za realno
            ride.save()
            return redirect('dashboard')
    else:
        form = RideRequestForm()
    return render(request, 'ride_request.html', {'form': form})

@login_required
def accept_ride(request, ride_id):
    if request.user.profile.user_type != 'driver':
        return redirect('dashboard')
    ride = Ride.objects.get(id=ride_id, status='requested', driver__isnull=True)
    ride.driver = request.user.profile
    ride.status = 'accepted'
    ride.save()
    return redirect('dashboard')
