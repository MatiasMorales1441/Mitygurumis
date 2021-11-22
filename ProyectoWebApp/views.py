from django.http import request
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

 
def send_email(mail):
    
    subject = 'feliz compra en mitygurumis'
    context = {'mail':mail}
    template = get_template('ProyectowebApp/correo.html')
    content = template.render(context)
    email = EmailMultiAlternatives(subject, #Titulo
                                    'Gracias por tu compra',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [mail]) #Destinatario

    email.attach_alternative(content, 'text/html')
    email.attach_file('./media/servicios/files/dasdasdas_H4YIp2R.pdf')
    email.send()
    


def index(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email(mail)

    return render(request,"ProyectowebApp/compra.html",{})

 



def webpay_plus_create(request):
    Servicio.objects.all()
    print("Webpay Plus Transaction.create")
    buy_order = str(1)
    session_id = str(13)
    amount = request.POST.get('precio')

    return_url=request.build_absolute_uri(location='commit-pay/')

    print('buy_order: {0}'.format(buy_order))
    print('amount: {0}'.format(amount))
    print('return_url: {0}'.format(return_url))
    print('request.headers: {0}'.format(request.headers))

    response = Transaction.create(buy_order, session_id, amount, return_url) 
    print('response: {0}'.format(response))

    return render(request, 'ProyectowebApp/send-pago.html', {'response': response, 'amount': amount})  

@csrf_exempt 
def commitpay(request):
    print('commitpay')
    print("request: {0}".format(request.POST))    
    token = request.POST.get('token_ws')

    TBK_TOKEN = request.POST.get('TBK_TOKEN')
    TBK_ID_SESION = request.POST.get('TBK_ID_SESION')
    TBK_ORDEN_COMPRA = request.POST.get('TBK_ORDEN_COMPRA')

    #TRANSACCIÓN REALIZADA
    if TBK_TOKEN is None and TBK_ID_SESION is None and TBK_ORDEN_COMPRA is None and token is not None:

        #APROBAR TRANSACCIÓN
        response = Transaction.commit(token=token)
        print("response: {}".format(response)) 

        status = response.status
        print("status: {0}".format(status))
        response_code = response.response_code
        print("response_code: {0}".format(response_code)) 
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
            return render(request, 'ProyectowebApp/commit-pay.html', {'transaction_detail': transaction_detail})
        else:
        #TRANSACCIÓN RECHAZADA            
            return HttpResponse('ERROR EN LA TRANSACCIÓN, SE RECHAZA LA TRANSACCIÓN.')
    else:
    #TRANSACCIÓN CANCELADA            
        return HttpResponse('ERROR EN LA TRANSACCIÓN, SE CANCELO EL PAGO.')


