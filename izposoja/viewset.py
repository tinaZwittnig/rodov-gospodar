from rest_framework import viewsets
from .models import *
from .serializers import *


class OpremaViewSet(viewsets.ModelViewSet):
    queryset = Oprema.objects.all()

    def get_serializer_class(self):
        # Define your HTTP method-to-serializer mapping freely.
        # This also works with CoreAPI and Swagger documentation,
        # which produces clean and readable API documentation,
        # so I have chosen to believe this is the way the
        # Django REST Framework author intended things to work:
        if self.request.method in ['GET']:
            # Since the ReadSerializer does nested lookups
            # in multiple tables, only use it when necessary
            return OpremaReadSerilizer
        return OpremaSerializer