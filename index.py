from rest_framework import viewsets, status
from rest_framework.response import Response

class IndexViewset(viewsets.ModelViewSet):
    
    def list(self, request, *args, **kwargs):
        res = {
            "api": "Teste API",
            "version": "1.0.0"
        }
        return Response(res, status=status.HTTP_200_OK)