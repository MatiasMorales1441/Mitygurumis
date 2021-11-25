from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),


    ###         PAGINAS DE LOS PRODUCTOS        ###  
    path('catalogo/',                   views.servicios, name="catalogo"),

        ##      ----    CERDTIO     ----    ##
    path('catalogo/cerdito/',           views.cerdito_producto),
    path('webpay-cerdito',              views.webpay_cerdito),
    path('commit-pay/cerdito',          views.commitpay_cerdito),
    path('commit-pay/correo-cerdito/',  views.correo_cerdito),
    
            ##      ----    GATITO  ----    ##
    path('catalogo/gatitos/',           views.gatitos_producto),
    path('webpay-gatitos',              views.webpay_gatitos),
    path('commit-pay/gatitos',          views.commitpay_gatitos),
    path('commit-pay/correo-gatitos/',  views.correo_gatitos),

            ##      ----    HURON   ----    ##
    path('catalogo/huron/',           views.huron_producto),
    path('webpay-huron',              views.webpay_huron),
    path('commit-pay/huron',          views.commitpay_huron),
    path('commit-pay/correo-huron/',  views.correo_huron),

            ##      ----    SIDNEY  ----    ##
    path('catalogo/sidney/',           views.sidney_producto),
    path('webpay-sidney',              views.webpay_sidney),
    path('commit-pay/sidney',          views.commitpay_sidney),
    path('commit-pay/correo-sidney/',  views.correo_sidney),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)