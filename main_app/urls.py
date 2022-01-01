from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('sabers/', views.sabers_index, name='sabers_index'),
  path('sabers/<int:saber_id>/', views.sabers_detail, name='sabers_detail'),
  path('sabers/create/', views.SaberCreate.as_view(), name='sabers_create'),
  path('sabers/<int:pk>/update/', views.SaberUpdate.as_view(), name='sabers_update'),
  path('sabers/<int:pk>/delete/', views.SaberDelete.as_view(), name='sabers_delete'),
  path('sabers/<int:saber_id>/add_repairing/', views.add_repairing, name='add_repairing'),
]