from django.shortcuts import render
from django.core.mail import send_mail
from .forms import EmailForm
# Create your views here.
def home(request):
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
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
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            send_mail(
                'Message from ' + form.cleaned_data['nume'] +
                ' (telefon: ' + form.cleaned_data['telefon'] + '| email: ' + form.cleaned_data['email'] + ')',  # subiect
                form.cleaned_data['mesaj'],  # mesaj
                form.cleaned_data['email'],  # from email
                ['suport.marut@gmail.com', 'gabrieldan2399@gmail.com',
                    'razvan_felecan@yahoo.com'],  # to email
            )
    form = EmailForm
    return render(request, "contact.html", {'form':form})

def ferestre(request):
    return render(request, "ferestre.html", {})

def usi(request):
    return render(request, "usi.html", {})

def rulouri(request):
    return render(request, "rulouri.html", {})

def accesorii(request):
    return render(request, "accesorii.html", {})

def aluplast(request):
    return render(request, "aluplast.html", {})

def euro(request):
    return render(request, "euro.html", {})

def synego(request):
    return render(request, "synego.html", {})

def geneo(request):
    return render(request, "geneo.html", {})


def articol1(request):
    return render(request, "articol1.html", {})

def articol2(request):
    return render(request, "articol2.html", {})

def articol3(request):
    return render(request, "articol3.html", {})
    
def articol4(request):
    return render(request, "articol4.html", {})

def articol5(request):
    return render(request, "articol5.html", {})

def articol6(request):
    return render(request, "articol6.html", {})
    
def articol7(request):
    return render(request, "articol7.html", {})
    
def articol8(request):
    return render(request, "articol8.html", {})

    
def articol9(request):
    return render(request, "articol9.html", {})
    
def articol10(request):
    return render(request, "articol10.html", {})

def termeni(request):
    return render(request, "termeni.html", {})
    
def utilizare(request):
    return render(request, "utilizare.html", {})

def protectie(request):
    return render(request, "protectie.html", {})

def a():
    pass

def b():
    pass