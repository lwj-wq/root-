import xadmin
from xadmin import views
from .models import User

class BaseSetting(object):
    '''
    xadmin的基础配置
    '''
    enabel_themes = True #开启主题功能
    use_bootswatch = True

class GlobalSettings(object):
    '''
    设置网站标题和页脚
    '''
    site_title = '1903C'
    site_footer = '1903C - poword by 1903'

xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)

class UserAdmin(object):
    '''
    后台展示内容
    后台可以搜索的内容
    后台过滤器可以使用的内容
    '''
    list_display = ['name','email','message']
    search_fields = ['name','email','message']
    list_fields = ['name','email','message','create_at']

xadmin.site.register(User,UserAdmin)









