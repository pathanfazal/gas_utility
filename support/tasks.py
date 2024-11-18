from django_q.models import Schedule
from .models import ServiceRequest
from django.utils.timezone import now

def resolve_service_request(request_id):
    """Background task to resolve a service request."""
    service_request = ServiceRequest.objects.get(id=request_id)
    service_request.resolve()
    print(f"Resolved ServiceRequest ID: {request_id} at {now()}")
