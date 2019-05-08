from django.urls import path
from zillna import views

urlpatterns = [
    path('zipless', views.update_zip),
    path('getzip', views.get_zip),

    #path('ranking', views.MiamiHeatStats.as_view()),
    #path('users/', views.UserList.as_view()),
    #path('users/<int:pk>/', views.UserDetail.as_view()),
    #path('heatculture/<int:pk>/', views.individual_game),

]