from django.shortcuts import render, HttpResponse
from app.models import Employees
from django.contrib import messages
from django.shortcuts import redirect


# Create your views here.
def index(request):
    emp = Employees.objects.all()
    context = {
        'emp':emp,
        }
    return render(request, 'index.html', context)
    # return render(request, 'index.html', {'employees': context})
    
    
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
    
        emp = Employees (
        name = name,
        email = email,
        address = address,
        phone = phone
        )
        emp.save()
        # return HttpResponse ("<h2>Data is saved successfully.</h2>")
        return redirect('index')
    return render(request, 'index.html')
