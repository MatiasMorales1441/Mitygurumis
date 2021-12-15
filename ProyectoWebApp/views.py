import builtins
from typing import Final, final
from django.core import mail
from django.db.models import query
from django.shortcuts import render, HttpResponse
from django.utils.functional import partition
from servicios.models import Servicio
from django.views.decorators.csrf import csrf_exempt
from blogs.models import Blog

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

import datetime as dt
from transbank.webpay.webpay_plus.transaction import Transaction



def home(request):
    servicio=Servicio.objects.all().last()
    blog = Blog.objects.all().first()
    return render(request,"ProyectowebApp/home.html",{"servicio": servicio, "blog": blog})




def tienda(request):
    
    return render(request,"ProyectowebApp/tienda.html")

def blog(request):
    blogs=Blog.objects.all()
    return render(request,"ProyectowebApp/blog.html", {"blogs": blogs})

def contacto(request):
    
    return render(request,"ProyectowebApp/contacto.html")

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request,"ProyectowebApp/catalogo.html", {"servicios": servicios})


def producto(request, id):
    servicio = Servicio.objects.get(id=id)
    return render(request,"ProyectoWebapp/producto.html",{"servicio":servicio})

def informacion(request, id):
    
    servicio = Servicio.objects.get(id=id)
    return render(request, 'ProyectowebApp/envio-correo_2.html', {"servicio":servicio, "mail":mail})

def webpay(request, id):
    servicio = Servicio.objects.get(id=id)
    buy_order = str(14123)
    session_id = request.POST.get('mail')
    amount = servicio.precio

    return_url = request.build_absolute_uri(location='commit-pay/')
    response = Transaction.create(buy_order, session_id, amount, return_url) 
    

    return render(request, 'ProyectowebApp/send-pago.html', {'response': response, 'amount': amount, "servicio":servicio, 'mail': mail})  


@csrf_exempt 
def commitpay(request,id):
    servicio = Servicio.objects.get(id=id)
    token = request.POST.get('token_ws')
    TBK_TOKEN = request.POST.get('TBK_TOKEN')
    TBK_ID_SESION = request.POST.get('TBK_ID_SESION')
    TBK_ORDEN_COMPRA = request.POST.get('TBK_ORDEN_COMPRA')
    
    nombre = servicio.nombre
    archivo = str("../Mitygurumis/media/servicios/files/"+str(nombre)+"-gurumi.pdf")

    #TRANSACCIÓN REALIZADA
    if TBK_TOKEN is None and TBK_ID_SESION is None and TBK_ORDEN_COMPRA is None and token is not None:
        
        #APROBAR TRANSACCIÓN
        response = Transaction.commit(token=token)
        status = response.status
        response_code = response.response_code
        #TRANSACCIÓN APROBADA
        if status == 'AUTHORIZED' and response_code == 0:

            state = ''
            if response.status == 'AUTHORIZED':
                state = 'Aceptado'
            pay_type = ''
            if response.payment_type_code == 'VD':
                pay_type = 'Tarjeta de Débito'
            
            mail = response.session_id
            subject = 'Muchas Gracias por tu Compra!'
            context = {'mail':mail}
            template = get_template('ProyectowebApp/correo.html')
            content = template.render(context)
            email = EmailMultiAlternatives(subject, #Titulo
                                            'Compra de Cerdito Gurumi!',
                                            settings.EMAIL_HOST_USER, #Remitente
                                            [mail]) #Destinatario
            email.attach_alternative(content, 'text/html')
            email.attach_file(archivo)
            email.send()

            amount = int(response.amount)
            amount = f'{amount:,.0f}'.replace(',', '.')
            transaction_date = dt.datetime.strptime(response.transaction_date, '%Y-%m-%dT%H:%M:%S.%fZ')
            transaction_date = '{:%d-%m-%Y %H:%M:%S}'.format(transaction_date)
            transaction_detail = {  'card_number': response.card_detail.card_number,
                                    'transaction_date': transaction_date,
                                    'state': state,
                                    'pay_type': pay_type,
                                    'amount': amount,
                                    'authorization_code': response.authorization_code,
                                    'buy_order': response.buy_order, }
            return render(request, 'ProyectowebApp/pago.html', {'transaction_detail': transaction_detail, 'servicio':servicio})
        else:
        #TRANSACCIÓN RECHAZADA            
            return HttpResponse('ERROR EN LA TRANSACCIÓN, SE RECHAZA LA TRANSACCIÓN.')
    else:
    #TRANSACCIÓN CANCELADA            
        return HttpResponse('ERROR EN LA TRANSACCIÓN, SE CANCELO EL PAGO.')

#def send_email(mail, id):
#    servicio = Servicio.objects.get(id=id)
#    subject = 'Muchas Gracias por tu Compra!'
#    context = {'mail':mail}
#    template = get_template('ProyectowebApp/correo.html')
#    content = template.render(context)
#    email = EmailMultiAlternatives(subject, #Titulo
#                                    'Compra de Cerdito Gurumi!',
#                                    settings.EMAIL_HOST_USER, #Remitente
#                                    [mail]) #Destinatario
#    email.attach_alternative(content, 'text/html')
#    pdf = servicio.objects.get('file')
#    email.attach_file(pdf)
#    email.send()

def correo(request, id):
    servicio = Servicio.objects.get(id=id)
    mail = request.POST.get('mail')
    
    nombre = servicio.nombre
    archivo = str("../Mitygurumis/media/servicios/files/"+str(nombre)+"-gurumi.pdf")
    print(nombre)
    print(archivo)

    if request.method == 'POST':
        subject = 'Muchas Gracias por tu Compra!'
        context = {'mail':mail}
        template = get_template('ProyectowebApp/correo.html')
        content = template.render(context)
        email = EmailMultiAlternatives(subject, #Titulo
                                        'Compra de Cerdito Gurumi!',
                                        settings.EMAIL_HOST_USER, #Remitente
                                        [mail]) #Destinatario
        email.attach_alternative(content, 'text/html')
        email.attach_file(archivo)
        email.send()
        
    return render(request,"ProyectowebApp/envio-correo.html",{"servicio":servicio, "mail":mail})




