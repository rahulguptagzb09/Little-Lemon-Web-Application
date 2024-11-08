from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index, name='index'),
    #path('menu/', views.MenuItemsView.as_view()),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('api-token-auth/', obtain_auth_token),
    path('bookings', views.bookings, name='bookings'), 
    path('reservations/', views.reservations, name="reservations"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('menu/', views.menu, name="menu"),

]