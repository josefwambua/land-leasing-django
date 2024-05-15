from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Land, Lease, Farmer
from .forms import LeaseForm
from django.contrib import messages

def land_list(request):
    lands = Land.objects.all()
    return render(request, 'leasing/land_list.html', {'lands': lands})

@login_required
def lease_land(request, land_id):
    land = get_object_or_404(Land, id=land_id)
    if request.method == 'POST':
        form = LeaseForm(request.POST)
        if form.is_valid():
            lease = form.save(commit=False)
            lease.lessee = request.user
            lease.save()
            messages.success(request, "Lease created successfully!")
            return redirect('land_list')
    else:
        form = LeaseForm(initial={'land': land})
    return render(request, 'leasing/lease_land.html', {'form': form, 'land': land})

@login_required
def my_leases(request):
    leases = Lease.objects.filter(lessee=request.user)
    return render(request, 'leasing/my_leases.html', {'leases': leases})

@login_required
def approve_lease(request, lease_id):
    lease = get_object_or_404(Lease, id=lease_id)
    if request.user == lease.land.farmer.user:
        lease.approved = True
        lease.save()
        messages.success(request, "Lease approved successfully!")
    return redirect('farmer_dashboard')

@login_required
def farmer_dashboard(request):
    farmer = get_object_or_404(Farmer, user=request.user)
    lands = Land.objects.filter(farmer=farmer)
    leases = Lease.objects.filter(land__in=lands)
    return render(request, 'leasing/farmer_dashboard.html', {'lands': lands, 'leases': leases})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})