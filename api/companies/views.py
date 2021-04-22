from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import CompanySerializers
from .models import Company


# Create your views here.
class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all().order_by("-last_update")
    serializer_class = CompanySerializers
    pagination_class = PageNumberPagination
