from django.urls import path
from .views import *

urlpatterns = [
    path('', CarListView.as_view(), name='home'),
    path('<slug:slug>/', CarDetailView.as_view(), name='home_detail'),

]