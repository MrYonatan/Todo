from .views import SignUpView, logout_success, home
from django.urls import path
urlpatterns = [
    
    path('signup/', SignUpView.as_view(), name='signup'),
    path('logout_success/', logout_success, name="logout_success"),
    path('', home, name="home" ),
    
]