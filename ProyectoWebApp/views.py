from django.shortcuts import render, HttpResponse
from django.utils.functional import partition
from servicios.models import Servicio
from blogs.models import Blog
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
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
    email.send()


def index(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        send_email(mail)

    return render(request,"ProyectowebApp/compra.html",{})

 
def send_user_mail(user):
    subject = 'Titulo del correo'
    template = get_template('templates/mi_template_correo.html')

    content = template.render({
        'user': user,
    })

    message = EmailMultiAlternatives(subject, #Titulo
                                    '',
                                    settings.EMAIL_HOST_USER, #Remitente
                                    [user.email]) #Destinatario

    message.attach_alternative(content, 'text/html')
    message.send()