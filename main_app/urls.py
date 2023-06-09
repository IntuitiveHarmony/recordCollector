from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>', views.records_detail, name='recordDetail'),
    path('bands/<int:band_id>', views.bands_detail, name='bandDetail'),
]