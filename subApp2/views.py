from django.shortcuts import render

# Create your views here.
def info_page(request):
    return render(request, 'Info.html')

def info_manage_page(request):
    return render(request,'Manage_info.html')

def info_progress_page(request):
    return render(request, 'Progress_info.html')

def info_cost_page(request):
    return render(request,'Cost_info.html')

def info_city_page(request):
    return render(request, 'City.html')
def info_hospital_page(request):
    return render(request, 'Hospital.html')

def info_seramic_page(request):
    return render(request, 'Seramic.html')