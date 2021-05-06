from django.shortcuts import render, redirect
from users.decorators import loginRequired
from django.views.generic.edit import FormView
from users.models import Users
from product.models import Product
from .models import Order
from .forms import OrderForm
from django.db import transaction
from django.utils.decorators import method_decorator
from django.views.generic import ListView

@method_decorator(loginRequired, name = 'dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/list'

    def form_valid(self, form):
        with transaction.atomic() : 
            prod = Product.objects.get(pk=form.data.get('product'))
            quantity = form.data.get('quantity')
            user = Users.objects.get(email=self.request.session.get('user'))

            order = Order(
                user = user,
                product = prod,
                quantity = quantity
            )
            order.save()

            prod.stock -= int(quantity)
            prod.save()

        return super().form_valid(form)

    def form_invalid(self, form) :
        return redirect('/product/detail'+str(form.data.get('product')))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update( {'request' : self.request } )
        return kw



@method_decorator(loginRequired, name = 'dispatch')
class OrderList(ListView):
    template_name = 'my_order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter( user__email = self.request.session.get('user') )
        return queryset