from django.http import HttpResponse
from .models import ItemList
from django.template import loader
from django.shortcuts import render,render_to_response
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy


def index(request):
    itemList =ItemList.objects.all()
    context={'itemList':itemList}
    return render(request,'itemdetails.html',{'itemList':itemList})

#Transaction details demo
#def getArticleDetails(request, article_id):
 #   return HttpResponse("<h1>Current product id: "+str(article_id)+"</h1>")

def addItem(request):
    itemList =ItemList.objects.all()
    productname=request.POST['productName']
    description=request.POST['description']
    wt=request.POST['wt']
    price=request.POST['price']
    if productname:
        add=ItemList(productName=productname,productDesc=description,productWt=wt,productPrice=price)
        add.save()

    return render(request,'itemdetails.html',{'itemList':itemList})
    #return reverse_lazy('itemDetails:itemDetails')


def search(request):
    if request.method=='POST':
        search_text=request.POST['search_text']
    else:
        search_text=''
    searcItemList =ItemList.objects.filter(productName__contains=search_text)
    return render_to_response('ajaxHtml.html',{'searchItemList':searcItemList})





class ItemListUpdate(UpdateView):
    model=ItemList
    fields=['productName','productDesc','productWt','productPrice']

class ItemListDelete(DeleteView):
    model=ItemList
    #redirecting url is here called as success url
    success_url = reverse_lazy('itemDetails:itemDetails')

