from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from . models import Menu,Booking
from . serializers import MenuSerializer,BookingSerializer
from rest_framework import generics,viewsets
# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset=Menu.objects.all()
    serializer_class=MenuSerializer
class BookingViewSet(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=BookingSerializer
    permission_classes = [IsAuthenticated]