from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>', views.games_detail, name='detail'),
    path('games/create/', views.GameCreate.as_view(), name='games_create'),
    path('games/<int:pk>/update', views.GameUpdate.as_view(), name='games_update'),
    path('games/<int:pk>/delete', views.GameDelete.as_view(), name='games_delete'),
    path('games/<int:game_id>/add_review/', views.add_review, name='add_review'),
    path('games/<int:game_id>/assoc_engine/<int:engine_id>/', views.assoc_engine, name='assoc_engine'),
    path('games/engine', views.EngineCreate.as_view(), name='engine_create'),
    path('games/<int:game_id>/engine_remove/<int:engine_id>', views.engine_remove, name='engine_remove')
]