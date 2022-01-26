from rest_framework import serializers
from models import *


class OmaraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Omara
        fields = '__all__'


class LokacijaSerializer(serializers.ModelSerializer):
    omara = OmaraSerializer()

    class Meta:
        model = Lokacija
        fields = [
            'id',
            'ime',
            'naslov',
            'omara'
        ]


class OpremaSerializer(serializers.ModelSerializer):
    lokacija = LokacijaSerializer()

    class Meta:
        model = Oprema
        fields = [
            'id',
            'naziv',
            'lokacija',
            'kolicina',
            'poskodbe',
            'opombe'
        ]


class FunkcijaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funkcija
        fields = '__all__'


class OsebaSerializer(serializers.ModelSerializer):
    funkcija = FunkcijaSerializer()

    class Meta:
        model = Oseba
        fields = ['id',
                  'email',
                  'telefonska_stevilka',
                  'ime',
                  'priimek',
                  'is_active',
                  'is_admin',]

class RezervacijaSerilizer(serializers.ModelSerializer):
    oseba = OsebaSerializer()
    oprema = OpremaSerializer()

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

class IzposojaSerilizer(serializers.ModelSerializer):
    rezervacija = RezervacijaSerilizer()

    class Meta:
        model = Izposoja
        fields = ['id',
                  'rezervacija',
                  'cas_izposoje',
                  'cas_vracila',
                  'opombe',
                  ]

class OdklepanjeSerializer(serializers.ModelSerializer):
    rezervacija = RezervacijaSerilizer()

    class Meta:
        model = Odklepanje
        fields = ['id',
                  'rezervacija',
                  'cas_odklepanja']