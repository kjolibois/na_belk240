from django.urls import path
from chaleurculture import views

urlpatterns = [
    path('update', views.update_page),
    path('ranking', views.MiamiHeatStats.as_view()),
    #path('heatculture/<int:pk>/', views.individual_game),

]