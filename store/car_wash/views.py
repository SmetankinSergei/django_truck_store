from django.shortcuts import render


def car_wash(request):
    return render(request, 'car_wash/car_wash.html')