"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from shop import views as errviews
from web import settings

urlpatterns = [
    path('shopeaze-admin/', admin.site.urls),  # admin panel
    path('accounts/', include('accounts.urls')),  # customer-accounts
    path('', include('shop.urls')),  # shop
    path('staff/', include('staffapp.urls')),  # staff
    path('payments/', include('payments.urls')),  # payments
    path('inventory-manager/', include('inventory.urls')),  # inventory
    path('sellers/', include('sellers.urls')),  # inventory
    path('mobile-pesa-api/v1/', include('mpesa_api.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = errviews.handler404
handler403 = errviews.handler403
handler500 = errviews.handler500
