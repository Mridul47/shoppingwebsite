from django.shortcuts import render
from django.views import View
from .models import Customer, Product, Cart, OrderPlaced
from.forms import CustomerRegistrationForm,CustomerProfileForm
from django.contrib import messages



class ProductView(View):
    def get(self,request):
        homeappliances = Product.objects.filter(category='H')
        device = Product.objects.filter(category='D')
        jeans = Product.objects.filter(category='J')
        return render(request, 'app/home.html',{'homeappliances':homeappliances,'device':device,'jeans':jeans})



class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html', {'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')


def address(request):
    add=Customer.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-dark'})

def orders(request):
 return render(request, 'app/orders.html')


 
def home_appliance(request , data=None):
    if data==None:
        homeappliances = Product.objects.filter(category='H')
    elif data =='Prestige' or data=='Taison':
        homeappliances=Product.objects.filter(category='H').filter(brand=data)
    elif data== 'below':
        homeappliances=Product.objects.filter(category='H').filter(discounted_price__lt=10000)
    elif data== 'above':
        homeappliances=Product.objects.filter(category='H').filter(discounted_price__gt=10000)

    return render(request, 'app/homeappliance.html', {'homeappliances':homeappliances})

def device(request , data=None):
    if data==None:
        devices = Product.objects.filter(category='D')
    elif data =='Redmi' or data=='Asus':
        devices=Product.objects.filter(category='D').filter(brand=data)
    elif data== 'below':
        devices=Product.objects.filter(category='D').filter(discounted_price__lt=10000)
    elif data== 'above':
        devices=Product.objects.filter(category='D').filter(discounted_price__gt=10000)

    return render(request, 'app/device.html', {'devices':devices})

def jeans(request , data=None):
    if data==None:
        jeanss = Product.objects.filter(category='J')
    elif data =='zara' or data=='Tara':
        jeanss=Product.objects.filter(category='J').filter(brand=data)
    elif data== 'below':
        jeanss=Product.objects.filter(category='J').filter(discounted_price__lt=10000)
    elif data== 'above':
        jeanss=Product.objects.filter(category='J').filter(discounted_price__gt=10000)

    return render(request, 'app/jeans.html', {'jeanss':jeanss})


def cotton(request , data=None):
    if data==None:
        cottons = Product.objects.filter(category='C')
    elif data =='Cr' or data=='Habibi':
        cottons=Product.objects.filter(category='C').filter(brand=data)
    elif data== 'below':
        cottons=Product.objects.filter(category='C').filter(discounted_price__lt=10000)
    elif data== 'above':
        cottons=Product.objects.filter(category='C').filter(discounted_price__gt=10000)

    return render(request, 'app/cotton.html', {'cottons':cottons})


class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})

    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congrats!! You have been registered successfully')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})

def checkout(request):
    return render(request, 'app/checkout.html')

class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'app/profile.html',{'form':form,'active':'btn-dark'})
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name=form.cleaned_data['name']
            locality=form.cleaned_data['locality']
            city=form.cleaned_data['city']
            state=form.cleaned_data['state']
            zipcode=form.cleaned_data['zipcode']
            reg= Customer(user=usr,name=name,locality=locality,city=city,state=state,zipcode=zipcode)
            reg.save()
            messages.success(request,'Congrats!! Profile has been updated')
        return render(request,'app/profile.html',{'form':form,'active':'btn-dark'})
