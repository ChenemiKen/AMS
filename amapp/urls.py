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
]