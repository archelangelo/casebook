from . import views as core_views
from django.urls import path, include

urlpatterns = [
    path('signup/', core_views.signup, name='signup'),
    path('account_activation_sent/', core_views.account_activation_sent, name='account_activation_sent'),
    path('activate/<uidb64>/<token>/', core_views.activate, name='activate'),
    path('profile/', core_views.view_profile, name='user_profile'),
]