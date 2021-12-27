from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('contacto/', views.contacto, name="contacto"),
       

    ###         PAGINAS DE LOS PRODUCTOS        ###  
    path('catalogo/',                               views.servicios,        name="catalogo"),
    path('catalogo/<int:id>/',                      views.producto,         name="producto"),
    path('catalogo/<int:id>/informacion/',          views.informacion,      name="informacion"),
    path('catalogo/<int:id>/informacion/webpay/',   views.webpay,           name="webpay"),
    path('catalogo/<int:id>/informacion/webpay/commit-pay/',          views.commitpay,        name="commit_pay"),
    path('webpay/commit-pay/correo/<int:id>/',      views.correo,           name="correo"),
    
    path('correo/<int:id>/', views.correo)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)