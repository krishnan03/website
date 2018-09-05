from tpage.models import oldTransaction,Transaction,UserDetails
from itemDetails.models import ItemList

val=Transaction.objects.all()
ReceiptVal=''
for data in val:
        new=data.productName+'~~'+data.productQty+'~~'+data.productWt+'~~'+data.productPrice+'||'
        ReceiptVal=ReceiptVal+new
oldval=oldTransaction(transaction=ReceiptVal)
oldval.save()
val=Transaction.objects.all()
val.delete()
print()