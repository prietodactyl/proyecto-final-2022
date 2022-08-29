from django.urls import path
from . import views

urlpatterns = [
    path('', views.calendario, name='calendario'),
    path('<int:year>/<str:month>/', views.calendario, name='calendario'),
    
    path('eventos/', views.all_events, name='eventos'),
    path('add_event/', views.add_event, name='add_event'),
    path('mostrar_evento/<event_id>', views.mostrar_evento, name='mostrar-evento'),
    
    path('ubicacion/', views.list_venues, name='list-venues'),
    
]