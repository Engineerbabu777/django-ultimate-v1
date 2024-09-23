
from django.urls import path
from . import views
# from .views import home, about, contact, services, blog, portfolio, team, pricing, faq, error_404, error_500

urlpatterns = [
    path('',views.home,name="home"),
    path('room/',views.room,name="room"),
    path('room/<str:pk>/',views.room_page,name="room_page"),
    path('room/create_room', views.create_room ,name="create_room"),
    path('room/update_room/<str:pk>/', views.update_room ,name="update_room"),
]
