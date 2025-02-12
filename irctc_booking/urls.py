
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/public/account/', include('account.urls')),
    path('api/user/booking/', include('booking.urls.user')),
    path('api/admin/booking/', include('booking.urls.admin')),
]
