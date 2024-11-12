from django.urls import path
from .views import GetCSVData, InsertCSVData, GetElectricVehicleData

urlpatterns = [
    path('get_csv/', GetCSVData.as_view(), name='get_csv_data'),
    path('insert_csv/', InsertCSVData.as_view(), name='insert_csv_data'),
    path('get_electric_vehicle_data/', GetElectricVehicleData.as_view(), name='get_electric_vehicle_data'),
]