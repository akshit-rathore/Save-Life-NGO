from django.shortcuts import redirect, render
from contactus.models import ContactUs
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'webpages/home.html')

def about(request):
    # sliders = Slider.objects.all()
    # data = {
    #     'sliders':sliders,
    # }
    return render(request, 'webpages/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        contactinfo = ContactUs(name=name, email=email, phone=phone, message=message)
        contactinfo.save()
        messages.success(request, "Thanks for reaching out!")
        return redirect('contact')

    return render(request, 'webpages/contact.html')
