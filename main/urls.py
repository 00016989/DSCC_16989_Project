from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    home,
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    FeedbackCreateView,
    FeedbackListView,
    FeedbackUpdateView,
    FeedbackDeleteView,
    register,
)

urlpatterns = [

    path('', home, name='home'),

    path('products/', ProductListView.as_view(), name='products'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),


    path('product/<int:pk>/feedback/add/',
         FeedbackCreateView.as_view(),
         name='feedback_create'),

    path('feedback/<int:pk>/edit/',
         FeedbackUpdateView.as_view(),
         name='feedback_update'),

    path('feedback/<int:pk>/delete/',
         FeedbackDeleteView.as_view(),
         name='feedback_delete'),

    path('feedback/list/',
         FeedbackListView.as_view(),
         name='feedback_list'),

    path('login/',
         auth_views.LoginView.as_view(template_name='main/login.html'),
         name='login'),

    path('logout/',
         auth_views.LogoutView.as_view(next_page='home'),
         name='logout'),

    path('register/', register, name='register'),
]
