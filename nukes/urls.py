from django.urls import path
from . import views

app_name='nukes'
urlpatterns=[
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('<str:category>/<uuid:pk>/',views.detail,name='detail'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.logins,name='login'),
    path('logout/',views.logouts,name='logout'),
    path('new/',views.create_item,name='create')
]