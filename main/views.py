from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Alwie Attar Elfandra',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)