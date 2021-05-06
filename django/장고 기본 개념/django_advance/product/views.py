from django.shortcuts import render
from django.views.generic.edit import FormView
from .models import Product
from .forms import RegisterForm
from django.utils.decorators import method_decorator
from users.decorators import adminRequired
from django.views.generic import ListView, DetailView

from rest_framework import generics, mixins
from .serializers import ProductSerializer

from order.forms import OrderForm

class ProductListAPI(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductDetailAPI(generics.GenericAPIView, mixins.RetrieveModelMixin):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all().order_by('id')
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


@method_decorator(adminRequired, name = 'dispatch')
class ProductCreate(FormView):
    template_name = 'create.html'
    form_class = RegisterForm
    success_url = '/'

    def form_valid(self, form):
        product = Product(
            name = form.data.get('name'),
            price = form.data.get('price'),
            description = form.data.get('description'),
            stock  = form.data.get('stock')
        )
        product.save()

        return super().form_valid(form)


class ProductList(ListView):
    model = Product
    template_name='list.html'
    context_object_name = 'product_list'

class ProductDetail(DetailView):
    template_name = "detail.html"
    queryset = Product.objects.all()
    context_object_name = 'product'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = OrderForm(self.request)
        return context