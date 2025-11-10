from django.contrib import admin
from django.urls import path
from django.urls import include
from Signup.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home, name='home_page'),  # optional /home/
    path('',home, name='home'),
    path('signup/', include('Signup.urls')),
]
