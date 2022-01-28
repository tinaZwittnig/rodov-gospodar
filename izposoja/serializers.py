from django.shortcuts import get_object_or_404
from rest_framework import serializers, viewsets, status, permissions
from rest_framework.response import Response

from .models import *


class LokacijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lokacija
        fields = [
            'id',
            'ime',
            'naslov',
        ]


class OmaraSerializer(serializers.ModelSerializer):


    class Meta:
        model = Omara
        fields = [
            'id',
            'naziv',
            'oznaka',
            'lokacija'

        ]

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data['lokacija'] = LokacijaSerializer(
                Lokacija.objects.get(pk=data['lokacija'])).data
            return data

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OpremaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oprema
        fields = [
            'id',
            'naziv',
            'omara',
            'polica',
            'kolicina',
            'poskodbe',
            'opombe'
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['omara'] = OmaraSerializer(
            Omara.objects.get(pk=data['omara'])).data
        return data


class FunkcijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funkcija
        fields = '__all__'


class OsebaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Oseba
        fields = ['id',
                  'email',
                  'telefonska_stevilka',
                  'ime',
                  'priimek',
                  'is_active',
                  'is_admin',
                  'funkcija']

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data['funkcija'] = FunkcijaSerializer(
                Funkcija.objects.get(pk=data['funkcija'])).data
            return data


class RezervacijaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rezervacija
        fields = ['id',
                  'oseba',
                  'oprema',
                  'cas',
                  'trajanje_izposoje',
                  'odobreno',
                  'opombe',
                  ]

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data['oseba'] = OsebaSerializer(
                Oseba.objects.get(pk=data['oseba'])).data
            data['oprema'] = OpremaSerializer(
                Oprema.objects.get(pk=data['oprema'])).data
            return data


class IzposojaSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Izposoja
        fields = ['id',
                  'rezervacija',
                  'cas_izposoje',
                  'cas_vracila',
                  'opombe',
                  ]

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data['rezervacija'] = RezervacijaSerializer(
                Rezervacija.objects.get(pk=data['rezervacija'])).data
            return data


class OdklepanjeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Odklepanje
        fields = ['id',
                  'rezervacija',
                  'cas_odklepanja']

        def to_representation(self, instance):
            data = super().to_representation(instance)
            data['rezervacija'] = RezervacijaSerializer(
                Rezervacija.objects.get(pk=data['rezervacija'])).data
            return data
