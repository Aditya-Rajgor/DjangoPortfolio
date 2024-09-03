# your_app/middleware.py
from django.http import HttpResponseForbidden

class AdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == '/traffic/' and not request.path.startswith('/admin/'):
            return HttpResponseForbidden("Access restricted. Please use the admin panel to access this page.")
        return self.get_response(request)
