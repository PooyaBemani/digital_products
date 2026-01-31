from rest_framework.views import APIView
from rest_framework.response import Response
from rest_frammework import status

from .models import Category,Product,File
from .serializers import CategorySerializer,ProductSerializer, FileSerializer

class ProductListView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)