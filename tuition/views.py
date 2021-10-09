from django.shortcuts import render
from tuition.models import profile, contact
from .forms import ContactForm


def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phone_no = request.POST['phone_no']
        message = request.POST['message']
        pro = profile(name=name, email=email, password=password, phone_no=phone_no, message=message)
        pro.save()
    return render(request, 'index.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST['name']
            phone = request.POST['phone']
            contact = request.POST['contact']



    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
