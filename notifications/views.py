from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Notification
from django_q.tasks import async_task

# View the list of notifications
@login_required
def notification_list(request):
    # Fetch only unread notifications for the logged-in user
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'notifications/notification_list.html', {'notifications': notifications})

# View a specific notification
@login_required
def notification_detail(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id, recipient=request.user)

    # Asynchronously mark the notification as read
    async_task('notifications.tasks.mark_as_read', notification.id)

    return render(request, 'notifications/notification_detail.html', {'notification': notification})
