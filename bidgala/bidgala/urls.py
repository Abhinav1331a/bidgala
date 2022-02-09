from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
# from accounts.views import CustomFormSignupView
from django.conf.urls import handler404
from django.conf.urls import handler500
import pages

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('', include('accounts.urls')),
    path('art/', include('products.urls')),
    path('accounts/', include('allauth.urls')),
    path('payments/', include('payments.urls')),
    path('community/', include('community.urls')),
    path('artist-forum/', include('community.urls')),
    path('', include('password.urls')),
    path('messages/', include('chat.urls')),
    path('orders/', include('orders.urls')),
    path('discover/', include('discover.urls')),
    path('blog/', include('discover.urls')),
    path('influencer/', include('influencer.urls')),
    path('survey/', include('survey.urls'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'pages.views.error_404'
handler500 = 'pages.views.error_500'

admin.site.site_header = 'Bidgala Admin'  