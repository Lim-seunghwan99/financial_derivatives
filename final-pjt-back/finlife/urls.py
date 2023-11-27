from django.urls import path
from . import views



urlpatterns = [
    path('save-deposit-products/', views.save_deposit_products),
    path('deposit-products/', views.deposit_products),
    path('saving-products/', views.saving_products),
    path('deposit-products/<str:fin_prdt_cd>/', views.get_deposit_product),
    path('saving-products/<str:fin_prdt_cd>/', views.get_saving_product),
    path('deposit-products-options/', views.deposit_product_options),
    path('saving-products-options/', views.saving_product_options),
    path('deposit-products-options/<str:fin_prdt_cd>/', views.deposit_product_option),
    path('saving-products-options/<str:fin_prdt_cd>/', views.saving_product_option),
    path('get-info/', views.get_info),
    path('get-info2/', views.get_info2),
]
