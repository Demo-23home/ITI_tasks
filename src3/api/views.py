# from rest_framework import viewsets
from .models import Trainee
from .serializers import TranieeSerializer
from rest_framework import generics


# class TraineeViewSet(viewsets.ModelViewSet):
#     queryset = Trainee.objects.all()
#     serializer_class = TraineeSerializer




class TranieeListCreateView(generics.ListCreateAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TranieeSerializer

class TranieeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trainee.objects.all()
    serializer_class = TranieeSerializer