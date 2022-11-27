from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

admin.site.site_header = "Tech Overflow Administration"
admin.site.site_title = "Tech Overflow Administration"

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('about/', views.about, name = "about"),

] + static(settings.MEDIA_URL, document_root  = settings.MEDIA_ROOT)
