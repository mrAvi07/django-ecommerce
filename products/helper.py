from django.shortcuts import render
from django.views import View
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



class ContactFormView(View):
    form_class = None
    template_name = "products/contact_form.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        super(ContactFormView, self).dispatch(*args, **kwargs)

    def get(self, *args, **kwargs):
        form = self.form_class
        return render(self.request, self.template_name, {'form':form})


    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            body = form.cleaned_data['body']

            message = f'Hello Admin, \n\nI am {name}. \n{body} \n\nRegards,\n{name}.'

            try:
                send_mail(subject, message, email, ['admin@gmail.com',])
                return HttpResponse("We will get back to you soon!")
            
            except BadHeaderError:
                return HttpResponse("Something went wrong. Try again")

        else:
            return HttpResponse("Invalid Form")
