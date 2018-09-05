from django.shortcuts import render
from django.http import HttpResponse
from .models import UserDetails,Transaction,oldTransaction
from itemDetails.models import ItemList
from django.urls import reverse_lazy
# Create your views here.

def index(request):
    userDetails=UserDetails.objects.all()
    itemList=ItemList.objects.all()
    context={'userDetails':userDetails,'itemList':itemList}
    return render(request,'tPage.html',context)

def verifyuser(request):
    mobileNo=request.POST['mobileNo']
    user=UserDetails.objects.filter(userMobileNo__contains=mobileNo)
    if user:
        context={'user':user}
    else:
        add=UserDetails(userMobileNo=mobileNo,userCurrentPoints=0)
        add.save()
        user=UserDetails.objects.filter(userMobileNo__contains=mobileNo)
        context={'user':user}
    return render(request,'tpage.html',context)

def addToCart(request):
    userDetails=UserDetails.objects.all()
    itemList=ItemList.objects.all()
    productID=request.POST['productID']
    productQty=request.POST['productQty']
    productID=productID[productID.index('ID:')+3:]
    productDetail=ItemList.objects.filter(pk=productID)
    productName=''
    productWt=''
    productPrice=0
    for val in productDetail:
        productName=val.productName
        productWt=val.productWt
        productPrice=val.productPrice
    productPrice=int(productPrice) * int(productQty)
    addCart=Transaction(productName=productName,productQty=productQty,productWt=productWt,productPrice=productPrice)
    addCart.save()
    transaction=Transaction.objects.all()
    totalItems=Transaction.objects.count()
    transactionTotalPrice=0
    for item in transaction:
        transactionTotalPrice=transactionTotalPrice+int(item.productPrice)
    context={'userDetails':userDetails,'itemList':itemList,'transaction':transaction,'totalItems':totalItems,'totalPrice':transactionTotalPrice}
    return render(request,'tpage.html',context)





def closeTransaction(request):
    val=Transaction.objects.all()
    ReceiptVal=''
    for data in val:
        new=data.productName+'~~'+data.productQty+'~~'+data.productWt+'~~'+data.productPrice+'||'
        ReceiptVal=ReceiptVal+new
    oldval=oldTransaction(transaction=ReceiptVal)
    oldval.save()
    val=Transaction.objects.all()
    val.delete()

    userDetails=UserDetails.objects.all()
    itemList=ItemList.objects.all()
    context={'userDetails':userDetails,'itemList':itemList}
    return render(request,'tpage.html',context)





