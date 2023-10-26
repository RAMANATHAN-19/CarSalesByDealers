from rest_framework import viewsets, mixins
from .models import CustomerDetails, Product, Sale
from .serializers import CustomerDetailsSerializer, ProductSerializer, SaleSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework import generics

class CustomerDetailsList(generics.ListCreateAPIView):
    queryset = CustomerDetails.objects.all()
    serializer_class = CustomerDetailsSerializer

class CustomerDetailsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerDetails.objects.all()
    serializer_class = CustomerDetailsSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

def get_customer_details_viewset():
    class CustomerDetailsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
        queryset = CustomerDetails.objects.all()
        serializer_class = CustomerDetailsSerializer
    return CustomerDetailsViewSet

def get_product_viewset():
    class ProductViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
    return ProductViewSet

def get_sale_viewset():
    class SaleViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
        queryset = Sale.objects.all()
        serializer_class = SaleSerializer
    return SaleViewSet


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })