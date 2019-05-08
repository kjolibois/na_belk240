from django.urls import path
from chaleurculture import views

urlpatterns = [
    path('update', views.update_page),
    path('ranking', views.MiamiHeatStats.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    #path('heatculture/<int:pk>/', views.individual_game),

]