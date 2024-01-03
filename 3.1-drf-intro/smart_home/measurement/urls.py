from django.urls import path

from measurement.views import SensorsView, MeasurementAddView, SensorView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementAddView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
]
