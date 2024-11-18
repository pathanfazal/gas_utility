from .models import Notification

def mark_as_read(notification_id):
    """Mark a specific notification as read."""
    try:
        notification = Notification.objects.get(id=notification_id)
        notification.is_read = True
        notification.save()
    except Notification.DoesNotExist:
        pass

def send_notification(recipient_id, message, notification_type):
    """Send a notification to a user asynchronously."""
    from django.contrib.auth.models import User
    recipient = User.objects.get(id=recipient_id)
    Notification.objects.create(
        recipient=recipient,
        message=message,
        notification_type=notification_type
    )
