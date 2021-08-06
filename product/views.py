from django.shortcuts import render
from django.views import generic
from .models import Offer, Location, Redemption


# Create your views here.
class OfferListView(generic.ListView):
    queryset = Offer.objects.all()
    template_name = 'product/offer.html'

class OfferDetailView(generic.DetailView):
    model = Offer
    template_name = 'product/offer_detail.html'

class RedeemDetailView(generic.DetailView):
    model = Redemption
    template_name = 'product/redeem_offer.html'

def maps(request):
    context = {
        'location' : Location.objects.all()
    }
    template_name = 'product/map.html'
    return render(request,template_name, context)
