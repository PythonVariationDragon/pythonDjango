from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.main,name='main'),
    # url(r'^market/(\d+)/(\d+)/(\d+)/$',views.market,name='market'),
    url(r'^market2/$',views.market2,name='market2'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^mine/$',views.mine,name='mine'),
    url(r'^register/$',views.register,name='register'),
    url(r'^saveuser/$',views.saveuser,name='saveuser'),
    url(r'^checkuserid$',views.checkuserid,name='checkuserid$'),
    url(r'^quit/$',views.quit,name='quit'),
    url(r'^login/$',views.login,name='login'),
    url(r'^checkuserlogin/$',views.checkuserlogin,name='checkuserlogin'),
]
