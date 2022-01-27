from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns

import  izposoja.views as views

urlpatterns = [
    path('oprema/<int:id>', views.OpremaDetail.as_view()),
    path('oseba/<int:id>', views.OsebaDetail.as_view()),
    path('rezervacija/<int:id>', views.RezervacijaDetail.as_view()),
    path('izposoja/<int:id>', views.IzposojaDetail.as_view()),
    path('odklepanje/<int:id>', views.OdklepanjeDetail.as_view()),
    path('oprema/', views.OpremaList.as_view()),
    path('omara/', views.OmaraList.as_view()),
    path('lokacija/', views.LokacijaList.as_view()),
    path('funkcija/', views.FunkcijaList.as_view()),
    path('oseba/', views.OsebaList.as_view()),
    path('rezervacija/', views.RezervacijaList.as_view()),
    path('izposoja/', views.IzposojaList.as_view()),
    path('odklepanje/', views.OdklepanjeList.as_view())
]
urlpatterns += [

]
urlpatterns = format_suffix_patterns(urlpatterns)
