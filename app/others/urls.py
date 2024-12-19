from django.urls import path

from app.views.auth.api import PartnerRegistrationView,AdminRegistrationView,CustomerRegistrationView



urlpatterns = [
    path('partner-register/', PartnerRegistrationView.as_view(), name='Register'),
    path('admin-register/', AdminRegistrationView.as_view(), name='Register'),
    path('customer-register/', CustomerRegistrationView.as_view(), name='Register'),
    # path('login/', UserLoginView.as_view(), name='user-login'),
]