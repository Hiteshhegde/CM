from . import views
from django.urls import path

urlpatterns = [
    path('offers/', views.OfferListView.as_view(), name = 'offer-home'),
    path('offers/<int:pk>', views.OfferDetailView.as_view(), name= 'offer-description'),
    path('offers/map', views.maps ,name= 'location'),
    path('redeems/<int:pk>', views.RedeemDetailView.as_view(), name= 'offer-redeem'),
]
