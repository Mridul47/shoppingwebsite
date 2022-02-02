from unicodedata import category
from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced

# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        homeappliances = Product.objects.filter(category='H')
        device = Product.objects.filter(category='D')
        jeans = Product.objects.filter(category='J')
        return render(request, 'app/home.html',{'homeappliances':homeappliances,'device':device,'jeans':jeans})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProduvtDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')


def home_appliance(request , data=None):
    if data==None:
        homeappliances = Product.objects.filter(category='H')
    elif data =='Prestige' or data=='Taison':
        homeappliances=Product.objects.filter(category='H').filter(brand=data)
    elif data== 'below':
        homeappliances=Product.objects.filter(category='H').filter(discounted_price__lt=10000)
    elif data== 'above':
        homeappliances=Product.objects.filter(category='H').filter(discounted_price__lt=10000)

    return render(request, 'app/homeappliance.html', {'homeappliances':homeappliances})

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
