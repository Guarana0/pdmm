from django.contrib import admin
from django.urls import path, include
from core import views # ou a importação que você usou

admin.site.login = views.MyAdminLoginView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]
