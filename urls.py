from django.urls import path
from . import views


app_name = 'rooms'
urlpatterns = [
    path('<int:building_id>/', views.list, name='list'),
    path('<int:building_id>/<int:room_id>/', views.detail, name='detail'),
    path('administration/', views.admin_add_stuff, name='adm'),
    path('administration/add_room', views.admin_add_room, name='add_room'),
    path('administration/add_building', views.admin_add_building, name='add_building'),
    path('administration/add_stuff', views.add_accept, name='add_accept'),
    path('administration/alter/<int:pk>', views.admin_alter, name='alter_page'),
    path('administration/alter_building/<int:pk>', views.alter_building, name='alter_building'),
    path('administration/alter_room/<int:pk>', views.alter_room, name='alter_room'),
    path('administration/alter_accept/<int:pk>', views.alter_accept, name='alter_accept'),
    path('administration/del_room/<int:pk>', views.admin_del_room, name='del_room'),
    # path('<int:building_id>/<int:room_id>/move/', views.move, name='move'),
]
