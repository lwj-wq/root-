from django.urls import path
import xadmin
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
]
