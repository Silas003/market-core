from django.urls import path
from . import views

app_name='dashboard'
urlpatterns=[
    path('',views.index,name='index'),
    path('delete/<str:category>/<int:pk>/',views.delete,name='delete')
]