# custom_middleware.py

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

class AdminFallbackMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            return self.get_response(request)

        # Check if the actual admin is available
        actual_admin = User.objects.filter(username=settings.ADMIN_USERNAME).first()

        if actual_admin and actual_admin.is_active:
            return self.get_response(request)

        # If actual admin is not available, check if the current user is designated to act as admin
        designated_admin_username = getattr(settings, 'DESIGNATED_ADMIN_USERNAME', None)

        if designated_admin_username and request.user.username == designated_admin_username:
            request.user.is_admin_fallback = True
            return self.get_response(request)

        # If neither the actual admin nor the designated user is available, deny access
        return HttpResponseForbidden("You are not authorized to access this page.")
