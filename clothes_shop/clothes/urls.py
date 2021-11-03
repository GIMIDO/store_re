from django.urls import path, include
from clothes import views

urlpatterns = [
    path('latest-clothes/', views.LatestClothesList.as_view()),
    path('clothes/<slug:category_slug>/<slug:clothes_slug>/', views.ClothesDetail.as_view()),
    path('clothes/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
