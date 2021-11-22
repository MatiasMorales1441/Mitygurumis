from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.home, name="home"),
    path('catalogo/', views.servicios, name="catalogo"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),
    path('catalogo/compra',views.index,name="compra"),
    path('webpay-plus-create',views.webpay_plus_create),
    path('commit-pay/',views.commitpay),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)