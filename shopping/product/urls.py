from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_page),
    path('login/', views.login),
    path('product/<int:id>/', views.set_product),
    path('all_products/', views.all_product),
    path('delete/<int:id>',views.delete_product,name='delete'),
    path('edit/<int:id>',views.update_product,name='edit')
]
