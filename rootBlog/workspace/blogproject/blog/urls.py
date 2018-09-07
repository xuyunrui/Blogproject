from django.conf.urls import url


from . import views


# 视图函数命名空间，告诉 Django 这个 urls.py 模块是属于 blog 应用的
app_name = 'blog'
urlpatterns = [
    # 正则匹配首页url，空字符串
    url(r'^$', views.index, name='index'),
    # 正则匹配文章详情页，url以 post/ 开头，后跟一个至少一位数的数字，并且以/符号结尾，如 post/1/，数字对应数据库中存储文章的id值
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
