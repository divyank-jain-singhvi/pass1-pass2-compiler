from django.contrib import admin
from django.urls import path ,include
from django.conf import settings          #for media foldwer connectionS
from django.conf.urls.static import static             #for media foldwer connectionS

from compiler.views import CodeView
from rest_framework import routers

route=routers.DefaultRouter()
route.register("",CodeView,basename='codeview')

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(route.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   #for media foldwer connectionS
