from django.conf import settings
from django.conf.urls.static import static 
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    # Django Admin
    path('admin/', admin.site.urls),

    # User management
    path('accounts/', include('allauth.urls')),

    # Local apps
    #path('accounts/', include('users.urls'))
    path('books/', include('books.urls')),
    path('', include('pages.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
