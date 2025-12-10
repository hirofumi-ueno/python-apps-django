from django.shortcuts import render


# def index(request):
#     return render(request, "index.html")

def index(request):
    context = {
        "name": "上野 広歩生",
    }
    return render(request, "index.html", context)
