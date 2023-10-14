from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('nukes.urls',namespace='nukes')),
    path('dashboard/',include('dashboard.urls',namespace='dashboard'))
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
