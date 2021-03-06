from django.db.models.query import ValuesIterable
from django.urls import path
from . import views

app_name = 'amapp'
urlpatterns=[
    path('', views.index, name='home'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_view, name='logout'),
    path('admin-dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('register-dashboard/<int:pk>', views.RegisterDashboard.as_view(), name='register_dashboard'),
    path('mysessions/<int:pk>', views.SessionListView.as_view(), name='my_sessions'),
    path('session_details/<int:pk>/<int:sid>',views.SessionDetailsView.as_view(),name='session_details'),
    path('addstudent',views.addstudent, name='addstudent'),
    path('createregister', views.CreateRegisterView.as_view(), name='create_register'),
    path('start_session',views.start_session, name='start-session'),
]