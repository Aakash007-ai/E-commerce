from django.shortcuts import render
#other imports
from .models import Item,OrderItem
from django.views.generic import ListView,DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.
# def home(request):#get request from server
#     context={
#         'items':Item.objects.all()
#     }
#     return render(request,'home.html',context=context)
#     #we get request for pages

class HomeView(ListView):
    model= Item
    pagination_by = 6 #no. of items on a page
    template_name = 'home.html'

# @login_required(login_url='../accounts/login/')   #login decorater
class ProductDetailView(DetailView):
    model = Item
    template_name = "detail.html"
    
@login_required(login_url='../accounts/login/')   #login decorater
def add_to_cart(request,slug):
    item=get_object_or_404(Item,slug=slug)
    order_item,created=OrderItem.objects.get_object_or_create(item=item,user=request.user,ordered=False)
    orer_q=Order.objects.filter(user=request.user,ordered=False)
    if order_q.exists():
        order=order_q[0]
        if order.items.filter(iter__slug=item.slug).exists():
            order_item +=1
            order_item.save()
            messages.info(request,"Item added to cart")
            return redirect("fronted:summary")
        else:
            messages.info(request,"Item added to cart")
            order.items.add(order_item)
            return redirect("fronted:summary")
    else:
        ordered_date = timezone.now()
        order =Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"Item added to cart")
        return redirect("fronted:summary")
# def testpage(request):
#     return render(request,'test.html')


