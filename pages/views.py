from django.shortcuts import render, get_object_or_404

from . models import Page

# Create your views here.

# from django.http import HttpResponse
def index(request, pagename):
    pagename = '/' + pagename   
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }
    return render(request, 'pages/page.html', context)

from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from . models import Page
from .forms import ContactForm

# Your index view

def need_help(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            con = get_connection('django.core.mail.backends.console.EmailBackend')
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email','noreply@example.com'), ['siteowner@example.com'], connection=con
                )
            return HttpResponseRedirect('/need_help?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True
        
    return render(request, 'pages/need_help.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})