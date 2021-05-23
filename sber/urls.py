from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from sber_calendar import views

urlpatterns = [
    path('', views.redirect_view),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
