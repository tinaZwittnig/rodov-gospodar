from django.urls import include, path
import  izposoja.views as views

urlpatterns = [
    path('oprema/', views.oprema, name='seznam_opreme')
]