from django.urls import path
from frontapp import views

urlpatterns = [

    path('home/', views.home, name='home'),
    path('frontend/', views.frontend, name='frontend'),
    path('servicedis/', views.servicedis, name='servicedis'),
    path('homedis/', views.homedis, name='homedis'),
    path('facecare/', views.facecare, name='facecare'),
    path('staffdis/', views.staffdis, name='staffdis'),
    path('facedisp/', views.facedisp, name='facedisp'),
    path('haircare/', views.haircare, name='haircare'),
    path('hairdisp/', views.hairdisp, name='hairdisp'),
    path('make/', views.make, name='make'),
    path('makeupdisp/', views.makeupdisp, name='makeupdisp'),
    path('log/', views.log, name='log'),
    path('sign/', views.sign, name='sign'),
    path('signpost/', views.signpost, name='signpost'),
    path('login/', views.login, name='login'),
    path('branchs/', views.branchs, name='branchs'),
    path('branchd/', views.branchd, name='branchd'),
    path('logout/', views.logout, name='logout'),
    path('pass_reset/', views.pass_reset, name='pass_reset'),

    # cart
    path('addCart/<str:pk>', views.addCart, name='addCart'),
    path('cart/', views.cartMain, name='cart'),
    path('deletecart/<str:pk>', views.deletecart, name='deletecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('checkoutpost/', views.checkoutpost, name='checkoutpost'),
    path('chk/', views.chk, name='chk'),
    path('chkpost/', views.chkpost, name='chkpost'),

]
