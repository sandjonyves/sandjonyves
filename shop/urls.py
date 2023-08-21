

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from shop import settings
from app.views import index,product_detail,add_to_cart
from account.views import signup,logout_user,login_user

urlpatterns = [

    path('sig/', signup,name="signup"),
    path('logout/', logout_user,name="logout"),
    path('login/', login_user,name="login"),
    path('', index,name="index"),
    path('admin/', admin.site.urls),
    path("product/<str:slug>/", product_detail, name="product_detail"),
    path("product/<str:slug>/add_to_cart", add_to_cart, name="add_to_cart")
] +static(settings.MEDIA_URL , document_root =settings.MEDIA_ROOT)
