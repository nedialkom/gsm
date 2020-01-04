from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('all-phones/', views.PhoneList.as_view(), name='GetPhoneList'),
    path('phone/', views.SetPhoneRating.as_view(), name='SetPhoneRating'),
    path('phone/<str:phoneHash>/', views.GetPhoneRating.as_view(), name='GetPhoneRating'),
    path('api-auth/', include('rest_framework.urls'), name='Authenticate'),
]
