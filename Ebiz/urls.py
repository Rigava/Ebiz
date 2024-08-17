"""
URL configuration for Ebiz project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ebizApp import views,adminViews

from django.conf.urls.static import static
from Ebiz import settings
urlpatterns = [
    # path('admin_old/', admin.site.urls),
    path('demo', views.demoPage),
    path('admin/', views.adminSignin,name="admin_login"),
    path('adminLogin', views.adminLoginProcess, name = "admin_login_process"),
    path('adminLogout', views.adminLogoutProcess, name = "admin_logout_process"),
    path('adminHome', adminViews.admin_home,name="admin_home"), 

    #CATEGORIES
    path('categoryList', adminViews.CategoriesListView.as_view(),name="category_list"),
    path('categoryCreate', adminViews.CategoriesCreate.as_view(),name="category_create"),
    path('categoryUpdate/<slug:pk>', adminViews.CategoriesUpdate.as_view(),name="category_update"),

    #SUBCATEGORIES
    path('sub_category_list',adminViews.SubCategoriesListView.as_view(),name="sub_category_list"),
    path('sub_category_create',adminViews.SubCategoriesCreate.as_view(),name="sub_category_create"),
    path('sub_category_update/<slug:pk>',adminViews.SubCategoriesUpdate.as_view(),name="sub_category_update"),

    #Merchant User
    path('merchant_create',adminViews.MerchantUserCreateView.as_view(),name="merchant_create"),
    path('merchant_list',adminViews.MerchantUserListView.as_view(),name="merchant_list"),
    path('merchant_update/<slug:pk>',adminViews.MerchantUserUpdateView.as_view(),name="merchant_update"),

    #Products
    path('product_create',adminViews.ProductView.as_view(),name="product_view"),
    path('product_list',adminViews.ProductListView.as_view(),name="product_list"),
    path('product_edit/<str:product_id>',adminViews.ProductEdit.as_view(),name="product_edit"),
    path('product_add_media/<str:product_id>',adminViews.ProductAddMedia.as_view(),name="product_add_media"),
    path('product_edit_media/<str:product_id>',adminViews.ProductEditMedia.as_view(),name="product_edit_media"),
    path('product_media_delete/<str:id>',adminViews.ProductMediaDelete.as_view(),name="product_media_delete"),
    path('product_add_stocks/<str:product_id>',adminViews.ProductAddStocks.as_view(),name="product_add_stocks"),
    path('file_upload',adminViews.file_upload,name="file_upload"),     
    
    #Customer User
    path('customer_create',adminViews.CustomerUserCreateView.as_view(),name="customer_create"),
    path('customer_list',adminViews.CustomerUserListView.as_view(),name="customer_list"),
    path('customer_update/<slug:pk>',adminViews.CustomerUserUpdateView.as_view(),name="customer_update"),

    #Store
    path('store',views.ProductListView.as_view(),name="store_list")


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
