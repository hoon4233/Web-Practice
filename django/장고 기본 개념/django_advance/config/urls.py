"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users.views import home, LoginView, logout, RegisterView
from product.views import ProductCreate, ProductList, ProductDetail
from order.views import OrderCreate, OrderList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('user/login/', LoginView.as_view()),
    path('user/logout/', logout),
    path('user/register/', RegisterView.as_view()),
    path('product/create/', ProductCreate.as_view()),
    path('product/list/', ProductList.as_view()),
    path('product/detail/<int:pk>', ProductDetail.as_view()),
    path('order/create/', OrderCreate.as_view()),
    path('order/list/', OrderList.as_view()),
]
