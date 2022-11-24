from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Item
from django.urls import reverse
from django.views import generic
from .forms import ItemForm, ListForm

# Create your views here.

def index(request):
    form = ItemForm()
    return render(request, "shiren/index.html",{'form': form } )


def list(request):
    form = ListForm()
    value  = request.POST.get('price')
    transaction = request.POST.get('transaction')
    item_type = request.POST.get('item_type')
    print(value, transaction, item_type)
    if transaction == 'buy':
        items = Item.objects.filter(item_type=item_type).filter(buy_price=value)
    if transaction == 'sell':
        items = Item.objects.filter(item_type=item_type).filter(sell_price=value)

    context ={'items': items, "form": form}
    return render(request, "shiren/list_items.html", context)


def check(request):
    print(request.POST)
    pass
