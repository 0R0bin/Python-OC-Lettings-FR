from django.contrib import admin
from django.urls import include
from django.urls import path

from oc_lettings_site.views import index

handler404 = 'oc_lettings_site.views.handler404'
handler500 = 'oc_lettings_site.views.handler500'

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', index, name='index'),
    path(r'lettings/', include('letting.urls')),
    path(r'profiles/', include('profiles.urls')),
]
