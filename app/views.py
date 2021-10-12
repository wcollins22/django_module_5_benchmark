from django.shortcuts import render
from app.forms import cal

# Create your views here.

def calc(request):
    form = cal(request.GET)
    if form.is_valid():
        a = form.cleaned_data["a"]
        b = form.cleaned_data["b"]
        answer = a + b
        return render(request, "cal.html", {"answer":answer})
    else:
        return render(request, "cal.html")

