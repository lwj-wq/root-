import xadmin
from django.urls import path,include
from django.views.generic.base import TemplateView
from apps.users.views import *
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 图片验证码 路由
    path('captcha/', include('captcha.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', TemplateView.as_view(template_name='index.html'), name='index')
]
