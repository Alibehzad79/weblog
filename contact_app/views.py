from django.shortcuts import render, redirect
from contact_app.models import ContactModel, ContactModelForm
from contact_app.forms import ContactForm
from datetime import datetime
# Create your views here.


def contact_page(request):
    template_name = 'contact/contact.html'
    try:
        contact = ContactModel.objects.last()
    except:
        contact = None
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            text = form.cleaned_data.get('text')
            new_contact = ContactModelForm.objects.create(name=name, email=email, subject=subject, text=text, date_sent=datetime.now())
            if new_contact is not None:
                new_contact.save()
                return redirect('contact:contact')
    else:
        form = ContactForm()
    context = {
        'contact': contact,
        'form': form,
    }
    return render(request, template_name, context)