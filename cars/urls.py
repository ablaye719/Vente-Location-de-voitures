
from django.urls import path
from .views import ListCarView,CreateCarVew,ManageCarView


app_name = 'cars'

urlpatterns = [
    path('', ListCarView.as_view(), name='listCar'),
    path('create/', CreateCarVew.as_view(), name='createCar'),
    path('manage/<int:pk>', ManageCarView.as_view(), name='manageCar')
]
