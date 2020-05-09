import xadmin
from django.urls import path,include,re_path
from django.views.generic.base import TemplateView
from apps.users.views import *
from apps.users import views
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # 图片验证码 路由
    path('captcha/', include('captcha.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('logout/',views.logout,name='logout'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    re_path('reset/(?P<active_code>.*)/', ResetView.as_view(), name='reset_pwd'),
    path('modify_pwd/', ModifyPwdView.as_view(), name='modify_pwd'),
]
