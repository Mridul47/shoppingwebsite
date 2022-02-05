from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm


urlpatterns = [
    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),


    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    path('home-appliance/', views.home_appliance, name='home-appliance'),
    path('home-appliance/<slug:data>', views.home_appliance, name='home-appliancedata'),

    path('device/', views.device, name='device'),
    path('device/<slug:data>', views.device, name='devicedata'),

    path('jeans/', views.jeans, name='jeans'),
    path('jeans/<slug:data>', views.jeans, name='jeansdata'),

    path('cotton/', views.cotton, name='cotton'),
    path('cotton/<slug:data>', views.cotton, name='cottondata'),

        
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'),name='passwordchange'),

    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),

    path('checkout/', views.checkout, name='checkout'),

    path('registration/',views.CustomerRegistrationView.as_view(), name="customerregistration")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
