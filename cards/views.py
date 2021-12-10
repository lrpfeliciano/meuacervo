from django.shortcuts import render
from .models import Card


# Create your views here.
def index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})


def ver_card(request, card_id):
    card = Card.objects.get(id=card_id)
    return render(request, 'cards/ver_card.html', {'card': card})
