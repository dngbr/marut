from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'Message from ' + form.cleaned_data['nume'] +
                ' (telefon: ' + form.cleaned_data['telefon'] + '| email: ' + form.cleaned_data['email'] + ')',  # subiect
                form.cleaned_data['mesaj'],  # mesaj
                form.cleaned_data['email'],  # from email
                ['suport.marut@gmail.com', 'gabrieldan2399@gmail.com',
                    'razvan_felecan@yahoo.com'],  # to email
            )
    form = EmailForm
    return render(request, "base.html", {'form':form})

def about(request):
    return render(request, "about.html", {})

def services(request):
    return render(request, "services.html", {})

def products(request):
    return render(request, "products.html", {})

def blog(request):
    return render(request, "blog.html", {})

def contact(request):
    return render(request, "contact.html", {})

def ferestre(request):
    return render(request, "ferestre.html", {})

def usi(request):
    return render(request, "usi.html", {})

def rulouri(request):
    return render(request, "rulouri.html", {})

def accesorii(request):
    return render(request, "accesorii.html", {})