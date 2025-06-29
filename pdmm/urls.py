from django.contrib import admin
from django.urls import path, include
from core import views # Importe as views, se ainda precisar delas diretamente aqui
from django.conf import settings
from django.conf.urls.static import static

admin.site.login = views.MyAdminLoginView.as_view()

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include('core.urls')),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)