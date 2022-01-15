
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('core.urls')),
    path("blog/", include('blog.urls')),
    path("accounts/", include('accounts.urls')),
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'core.views.custom_page_not_found_view'
handler500 = 'core.views.custom_error_view'
handler403 = 'core.views.custom_permission_denied_view'
handler400 = 'core.views.custom_bad_request_view'