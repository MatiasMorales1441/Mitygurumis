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
    
    return render(request,"ProyectowebApp/home.html")

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request,"ProyectowebApp/catalogo.html", {"servicios": servicios})

def tienda(request):
    
    return render(request,"ProyectowebApp/tienda.html")

def blog(request):
    blogs=Blog.objects.all()
    return render(request,"ProyectowebApp/blog.html", {"blogs": blogs})

def contacto(request):
    
    return render(request,"ProyectowebApp/contacto.html")

 





###         PAGINAS DE LOS PRODUCTOS        ###



    ##      ----    CERDTIO     ----    ##

def cerdito_producto(request):
    return render(request,"ProyectowebApp/productos/cerdito/cerdito.html")

def webpay_cerdito(request):
    Servicio.objects.all()
    buy_order = str(12312)
    session_id = str(1441)
    amount = 1000

    return_url=request.build_absolute_uri(location='commit-pay/cerdito')
    response = Transaction.create(buy_order, session_id, amount, return_url) 

    return render(request, 'ProyectowebApp/productos/cerdito/send-pago.html', {'response': response, 'amount': amount})  

@csrf_exempt 
def commitpay_cerdito(request):
    token = request.POST.get('token_ws')
    TBK_TOKEN = request.POST.get('TBK_TOKEN')
    TBK_ID_SESION = request.POST.get('TBK_ID_SESION')
    TBK_ORDEN_COMPRA = request.POST.get('TBK_ORDEN_COMPRA')

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
            return render(request, 'ProyectowebApp/productos/cerdito/pago-cerdito.html', {'transaction_detail': transaction_detail})
        else:
        #TRANSACCIÓN RECHAZADA            
            return HttpResponse('ERROR EN LA TRANSACCIÓN, SE RECHAZA LA TRANSACCIÓN.')
    else:
    #TRANSACCIÓN CANCELADA            
        return HttpResponse('ERROR EN LA TRANSACCIÓN, SE CANCELO EL PAGO.')


def send_email_cerdito(mail):
    subject = 'Muchas Gracias por tu Compra!'
    context = {'mail':mail}
    template = get_template('ProyectowebApp/correo.html')
    content = template.render(context)
    email = EmailMultiAlternatives(subject, #Titulo
                                    'Compra de Cerdito Gurumi!',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [mail]) #Destinatario
    email.attach_alternative(content, 'text/html')
    email.attach_file('ProyectoWebApp/static/ProyectoWebApp/archivos/cerdito-gurumi.pdf')
    email.send()

def correo_cerdito(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email_cerdito(mail)

    return render(request,"ProyectowebApp/productos/cerdito/envio-correo.html",{})

    ##      ----    GATITOS     ----    ##

def gatitos_producto(request):
    return render(request,"ProyectowebApp/productos/gatitos/gatitos.html")

def webpay_gatitos(request):
    Servicio.objects.all()
    buy_order = str(12312)
    session_id = str(1441)
    amount = 1000

    return_url=request.build_absolute_uri(location='commit-pay/gatitos')
    response = Transaction.create(buy_order, session_id, amount, return_url) 

    return render(request, 'ProyectowebApp/productos/gatitos/send-pago.html', {'response': response, 'amount': amount})  

@csrf_exempt 
def commitpay_gatitos(request):
    token = request.POST.get('token_ws')
    TBK_TOKEN = request.POST.get('TBK_TOKEN')
    TBK_ID_SESION = request.POST.get('TBK_ID_SESION')
    TBK_ORDEN_COMPRA = request.POST.get('TBK_ORDEN_COMPRA')

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
            return render(request, 'ProyectowebApp/productos/gatitos/pago-gatitos.html', {'transaction_detail': transaction_detail})
        else:
        #TRANSACCIÓN RECHAZADA            
            return HttpResponse('ERROR EN LA TRANSACCIÓN, SE RECHAZA LA TRANSACCIÓN.')
    else:
    #TRANSACCIÓN CANCELADA            
        return HttpResponse('ERROR EN LA TRANSACCIÓN, SE CANCELO EL PAGO.')


def send_email_gatitos(mail):
    subject = 'feliz compra en mitygurumis'
    context = {'mail':mail}
    template = get_template('ProyectowebAppcorreo.html')
    content = template.render(context)
    email = EmailMultiAlternatives(subject, #Titulo
                                    'Compra de gatitos Gurumi!',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [mail]) #Destinatario
    email.attach_alternative(content, 'text/html')
    email.attach_file('ProyectoWebApp/static/ProyectoWebApp/archivos/gatitos-gurumi.pdf')
    email.send()

def index(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email_gatitos(mail)

    return render(request,"ProyectowebApp/productos/gatitos/envio-correo.html",{})
    ##      ----    HURON       ----    ##

def huron_producto(request):
    return render(request, "ProyectowebApp/productos/huron/huron.html")

    ##      ----    SIDNEY      ----    ##

def sidney_producto(request):
    return render(request, "ProyectowebApp/productos/sidney/sidney.html")



