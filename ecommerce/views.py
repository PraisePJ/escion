from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'home.html')

def Shoes(request):
    return render(request, 'shoes.html')

def Watches(request):
    return render(request, 'watches.html')

def Phones(request):
    return render(request, 'phones.html')

def Laptops(request):
    return render(request, 'laptops.html')

def HealthCare(request):
    return render(request, 'health_care.html')

def HairGrooming(request):
    return render(request, 'hair_grooming.html')

def Cosmetics(request):
    return render(request, 'cosmetics.html')

def Clothes(request):
    return render(request, 'clothes.html')

def Books(request):
    return render(request, 'books.html')
