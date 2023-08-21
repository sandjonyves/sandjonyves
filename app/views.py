from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import cart, Product,Order
# Create your views here.
from django.shortcuts import redirect
def index(request):
    products=Product.objects.all()
    return render(request, 'store/index.html',context={
        'products':products
    })

def product_detail( request,slug):

   product =  get_object_or_404(Product,slug=slug)

   return render(request, "store/detail.html",context={"product":product})

def add_to_cart(request,slug):
   user= request.user
   product=get_object_or_404(Product,slug=slug)
   carts, _ =cart.objects.get_or_create(user=user)
   order , created = Order.objects.get_or_create(user=user, product=product)

   if created:
      carts.orders.add(order)
      carts.save()

   else:
      order.quantity += 1
      order.save()

   return redirect(reverse("product_detail",kwargs={ "slug":slug}))     