from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=250, label="Your Name")
    email = forms.EmailField(label="Your Email")
    subject = forms.CharField(widget=forms.Textarea, label="Subject")
    body = forms.CharField(widget=forms.Textarea, label="Message")