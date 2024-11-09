
from django.urls import path,include


urlpatterns = [
   path('Basics/',include('Basics.urls')),
   path('Admin/',include('Admin.urls'))
]