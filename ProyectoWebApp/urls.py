from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.home, name="home"),
    path('catalogo/', views.servicios, name="catalogo"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),


    ###         PAGINAS DE LOS PRODUCTOS        ###  

        ##      ----    CERDTIO     ----    ##
    path('catalogo/cerdito/', views.cerdito_producto),
    path('webpay-cerdito',views.webpay_cerdito),
    path('commit-pay/cerdito',views.commitpay_cerdito),
    path('commit-pay/correo-cerdito/',views.correo_cerdito),
    
            ##      ----    GATITO  ----    ##
    path('catalogo/gatitos/', views.gatitos_producto),
    path('webpay-gatitos',views.webpay_gatitos),
    path('commit-pay/gatitos',views.commitpay_gatitos),
    path('commit-pay/correo-cerdito/',views.index,name="compra"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)