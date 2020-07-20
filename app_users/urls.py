from django.urls import path
from .views import Login, Registration
app_name = 'app_users'

urlpatterns = [
    path('login/', Login.as_view()),
    path('registration/', Registration.as_view())
]
