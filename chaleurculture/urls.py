from django.urls import path
from chaleurculture import views

urlpatterns = [
    path('update', views.update_page),
    #path('heatculture/ranking', views.TextAPIView),
    #path('heatculture/<int:pk>/', views.individual_game),

]