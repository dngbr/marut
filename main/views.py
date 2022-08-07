from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST['message-name']
        email = request.POST['message-email']
        phone = request.POST['message-phone']
        message = request.POST['message']
        send_mail(
            'Message from ' + name +
            '(nr.tel.: ' + phone + '| email: ' + email + ')',  # subiect
            message,  # mesaj
            email,  # from email
            ['suport.marut@gmail.com', 'gabrieldan2399@gmail.com',
                'razvan_felecan@yahoo.com'],  # to email
        )
        return render(request, "base.html", {})
    else:
        return render(request, "base.html", {})