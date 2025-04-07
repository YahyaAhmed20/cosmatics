from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('admin/', admin.site.urls),

    # المصادقة عبر allauth و Django auth
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('i18n/setlang/', set_language, name='set_language'),

    
    # تأكد من عدم تكرار هذا السطر
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # باقي التطبيقات
    path('about/', include('about.urls', namespace='about')),
    path('services/', include('services.urls', namespace='services')),
    path('contact-us/', include('contact.urls', namespace='contact')),
    path('', include('home.urls', namespace='home')),
]

# إعدادات الملفات الثابتة (في وضع التطوير)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
