from django.urls import path,include
from django.views.generic.base import TemplateView
import xadmin
from apps.users.views import LoginView
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name='login')
]
