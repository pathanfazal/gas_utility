from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),  # Includes common app URLs (login, register, home)
    path('dashboard/', include('customer.urls')),  # Includes customer app URLs (dashboard, service requests)
    path('support/', include('support.urls')),  # Includes support app URLs (manage requests, resolve tickets)
    path('reports/', include('reports.urls')),  # Includes report-related URLs (generate/download reports)
    path('notifications/', include('notifications.urls')),  # Includes notifications URLs (view notifications)
    path('logs/', include('logs.urls')),  # Includes logs URLs (view system logs)

    # Logout route
    path('logout/', LogoutView.as_view(), name='logout'),  # Directly handle logout
]

# Serve media files during development (if required)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
