from django.urls import path;
from DemoApp1 import views;

urlpatterns = [
    path('third/',views.f1),
    path('fourth/',views.f2),

];
