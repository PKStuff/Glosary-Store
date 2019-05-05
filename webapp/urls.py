from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/',views.sold_item, name='sold_item'),
    path('index/start/', views.Start_Shop, name='Start_Shopping'),
    path('index/end/', views.End_Shop, name='End_Shopping')
]
