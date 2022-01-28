from rest_framework import generics, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from .serializers import *


class OpremaList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Oprema.objects.all()
    serializer_class = OpremaSerializer


class OpremaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oprema.objects.all()
    serializer_class = OpremaSerializer


class OmaraList(generics.ListCreateAPIView):
    queryset = Omara.objects.all()
    serializer_class = OmaraSerializer


class OmaraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Omara.objects.all()
    serializer_class = OmaraSerializer


class LokacijaList(generics.ListCreateAPIView):
    queryset = Lokacija.objects.all()
    serializer_class = LokacijaSerializer


class LokacijaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lokacija.objects.all()
    serializer_class = LokacijaSerializer


class OsebaList(generics.ListCreateAPIView):
    queryset = Oseba.objects.all()
    serializer_class = OsebaSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OsebaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Oseba.objects.all()
    serializer_class = OsebaSerializer



class FunkcijaList(generics.ListCreateAPIView):
    queryset = Funkcija.objects.all()
    serializer_class = FunkcijaSerializer


class FunkcijaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Funkcija.objects.all()
    serializer_class = FunkcijaSerializer


class RezervacijaList(generics.ListCreateAPIView):
    queryset = Rezervacija.objects.all()
    serializer_class = RezervacijaSerializer


class RezervacijaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rezervacija.objects.all()
    serializer_class = RezervacijaSerializer


class IzposojaList(generics.ListCreateAPIView):
    queryset = Izposoja.objects.all()
    serializer_class = IzposojaSerilizer


class IzposojaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Izposoja.objects.all()
    serializer_class = IzposojaSerilizer


class OdklepanjeList(generics.ListCreateAPIView):
    queryset = Odklepanje.objects.all()
    serializer_class = OdklepanjeSerializer


class OdklepanjeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Odklepanje.objects.all()
    serializer_class = OdklepanjeSerializer

