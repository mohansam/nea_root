from django.shortcuts import render


# Your index view

def need_help(request):
    return render(request, 'pages/need_help.html')