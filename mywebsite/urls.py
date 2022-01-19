
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# sitemap
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import PostSitemap


sitemaps = {
    'posts': PostSitemap
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('core.urls')),
    path("blog/", include('blog.urls')),
    path("accounts/", include('accounts.urls')),
    # ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # sitemap
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'core.views.custom_page_not_found_view'
handler500 = 'core.views.custom_error_view'
handler403 = 'core.views.custom_permission_denied_view'
handler400 = 'core.views.custom_bad_request_view'