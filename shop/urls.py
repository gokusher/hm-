from product import views
from product import views as product_views
from django.urls import path, include
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', include('jazzmin.urls')),
    path('admin/', admin.site.urls),
    path('', product_views.main_view, name='main_view'),
    path('products/', product_views.products_view, name='products_view'),
    path('admin/', admin.site.urls),
    path('hello/', views.hello, name='hello'),
    path('current_date/', views.current_date, name='current_date'),
    path('goodbye/', views.goodbye, name='goodbye'),
]
