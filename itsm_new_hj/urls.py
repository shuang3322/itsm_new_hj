"""itsm_new_hj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from customer import views as customer_views
from producer import views as producer_views
from indexapp import views as index_views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('customer', customer_views.visit),
    path('priducer', producer_views.visit),
    path('', index_views.visit),


]

#测试新的东西