from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name")
    phone = forms.CharField(max_length=12, label="Your Phone")
    contact = forms.CharField( label="Contact")
    contact = forms.EmailField( label="Email")
