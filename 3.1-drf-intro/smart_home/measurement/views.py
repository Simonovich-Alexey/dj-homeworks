from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementAddSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementAddView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementAddSerializer


class ChangeRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorDetailSerializer
        if self.request.method == 'PATCH':
            return SensorSerializer


class SensorView(ChangeRetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
