
from django.urls import path,include
from vamsi import views
urlpatterns = [

    path('',views.sai),
    path('emp',views.salman),
    path('HR',views.satya)
]