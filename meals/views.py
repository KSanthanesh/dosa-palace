from django.shortcuts import render, redirect
from .models import Meals, Reserve
from .forms import ReserveForm


def home(request):
    return render(request, 'meals/home.html')


def get_meal_list(request):
    meal_list = Meals.objects.all()

    context = {
        'meal_list': meal_list,
    }

    return render(request, 'meals/list.html', context)


def get_meal_detail(request, m_id):
    meal_detail = Meals.objects.get(id=m_id)

    context = {
        'meal_detail': meal_detail,
    }

    return render(request, 'meals/detail.html', context)


def contact(request):
    return render(request, 'meals/contact.html')


def reserve(request):
    reserves = Reserve.objects.all()
    context = {
        'reserves': reserves
        }
    return render(request, 'meals/reserve.html', context)


def add_reserve(request):
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_reserve')
    form = ReserveForm()
    context = {
            'form': form
        }

    return render(request, 'meals/add_reserve.html', context)


# def edit_reserve(request, name):
#     reservation = get_object_or_404(Reserve, name=name)
#     if request.method == "POST":
#         form = ReserveForm(request.POST, instance=reservation)
#         if form.is_valid():
#             form.save()
#             return redirect('reserve')

#     form = ReserveForm(instance=reservation)
#     context = {
#             'form': form
#         }

#     return render(request, 'meals/edit_reserve.html', context)
