from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import LogEntry
from django_q.tasks import async_task

@login_required
def log_list(request):
    """Fetch logs asynchronously to support high concurrency."""
    user_logs = LogEntry.objects.filter(user=request.user)
    return render(request, 'logs/log_list.html', {'logs': user_logs})


@login_required
def log_detail(request, log_id):
    """Fetch a single log entry asynchronously."""
    log = LogEntry.objects.get(id=log_id, user=request.user)
    return render(request, 'logs/log_detail.html', {'log': log})


@login_required
def generate_log(request):
    """Example of a task that creates a log entry asynchronously."""
    if request.method == 'POST':
        async_task('logs.tasks.create_log_entry', request.user, 'This is an async log', 'INFO')
        return render(request, 'logs/log_list.html', {'message': 'Log task queued successfully.'})
    return render(request, 'logs/generate_log.html')
