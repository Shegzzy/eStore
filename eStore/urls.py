from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

admin.site.index_title = "DenPolyLimited Admin"
admin.site.site_title = "DenPolyLimited Admin"

urlpatterns = [
    path("denpoly.admin/", admin.site.urls),
    path("", include("store.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
