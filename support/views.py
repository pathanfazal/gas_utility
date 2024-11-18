from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm, ServiceRequestFilterForm
from django_q.tasks import async_task

@login_required
def dashboard(request):
    # Allow filtering by status
    filter_form = ServiceRequestFilterForm(request.GET)
    status_filter = request.GET.get('status')
    if status_filter:
        unresolved_requests = ServiceRequest.objects.filter(status=status_filter)
    else:
        unresolved_requests = ServiceRequest.objects.filter(status='Pending')
    return render(request, 'support/dashboard.html', {
        'unresolved_requests': unresolved_requests,
        'filter_form': filter_form,
    })

@login_required
def manage_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('support_dashboard')
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'support/manage_request.html', {
        'service_request': service_request,
        'form': form,
    })

@login_required
def resolve_request(request, request_id):
    service_request = get_object_or_404(ServiceRequest, id=request_id)

    # Use Django Q to resolve in the background
    async_task('support.tasks.resolve_service_request', service_request.id)

    return redirect('support_dashboard')
