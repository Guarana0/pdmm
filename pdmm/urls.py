from django.contrib import admin
from django.urls import path, include
from core import views # ou a importação que você usou

admin.site.login = views.MyAdminLoginView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('core.urls')),
    path('admin/login/', views.MyAdminLoginView.as_view(), name='admin_login'),
    path('admin/password_change/', views.MyAdminPasswordChangeView.as_view(), name='admin_password_change'),
]

# Error handlers (use corresponding templates when DEBUG = False)
# Ensure you have: 400.html, 403.html, 404.html, 500.html in your templates root.
handler400 = 'django.views.defaults.bad_request'
handler403 = 'django.views.defaults.permission_denied'
handler404 = 'django.views.defaults.page_not_found'
handler500 = 'django.views.defaults.server_error'
