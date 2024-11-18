from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest, AccountDetails
from .forms import ServiceRequestForm

# Customer dashboard view
@login_required
def dashboard(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'customer/dashboard.html', {'user_requests': user_requests})

# View and manage service requests
@login_required
def service_requests_list(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'customer/service_requests_list.html', {'user_requests': user_requests})

# Submit a new service request
@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Associate with the current user
            service_request.save()
            return redirect('service_requests_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'customer/submit_service_request.html', {'form': form})
