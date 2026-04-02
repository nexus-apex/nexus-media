from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('contents/', views.content_list, name='content_list'),
    path('contents/create/', views.content_create, name='content_create'),
    path('contents/<int:pk>/edit/', views.content_edit, name='content_edit'),
    path('contents/<int:pk>/delete/', views.content_delete, name='content_delete'),
    path('mediachannels/', views.mediachannel_list, name='mediachannel_list'),
    path('mediachannels/create/', views.mediachannel_create, name='mediachannel_create'),
    path('mediachannels/<int:pk>/edit/', views.mediachannel_edit, name='mediachannel_edit'),
    path('mediachannels/<int:pk>/delete/', views.mediachannel_delete, name='mediachannel_delete'),
    path('publishschedules/', views.publishschedule_list, name='publishschedule_list'),
    path('publishschedules/create/', views.publishschedule_create, name='publishschedule_create'),
    path('publishschedules/<int:pk>/edit/', views.publishschedule_edit, name='publishschedule_edit'),
    path('publishschedules/<int:pk>/delete/', views.publishschedule_delete, name='publishschedule_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
