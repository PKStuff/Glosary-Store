from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/',views.sold_item, name='sold_item'),
    path('index/start/', views.Start_Shop, name='Start_Shopping'),
    path('index/end/', views.End_Shop, name='End_Shopping'),
    path('delete/<int:item_id>/',views.delete_item, name='delete_item'),
    path('update/<int:item_id>/', views.update_item, name='update_item'),
]
