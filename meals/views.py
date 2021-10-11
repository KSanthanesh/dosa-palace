from django.shortcuts import render, redirect, get_object_or_404
from .models import Meals, Reserve, MasterTable
from .forms import ReserveForm
from django.contrib import messages
from allauth.account.utils import user_display
from django import template
# from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag(name="user_display")
def user_display_tag(user):

    return user_display(user)
# allauth.account.user


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

def contact_reply(request):
    return render(request, 'meals/contact_reply.html')


def add_reserve(request):
    if request.method == "POST":
        form = ReserveForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Table Booked successfully')
            return redirect('view_reserve')
    form = ReserveForm()
    context = {
            'form': form
        }

    return render(request, 'meals/add_reserve.html', context)



def get_total_tables(request):
    total_table = MasterTable.objects.all()

    context = {
        'total_table': total_table,
    }

    return render(request, 'meals/add_reserve.html', context)


def view_reserve(request, *args, **kwargs):
    reserves = Reserve.objects.all()
    context = {
        'reserves': reserves
        }
    return render(request, 'meals/view_reserve.html', context)


def user_list(request):
    ul = Reserve.objects.all()
    context = {
        'ul': ul
        }
    return render(request, 'meals/user_list.html', context)


def edit_reserve(request, meal_id):
    reservation = get_object_or_404(Reserve, id=meal_id)
    
    if request.method == "POST":
        form = ReserveForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('view_reserve')

    form = ReserveForm(instance=reservation)
    context = {
            'form': form
        }

    return render(request, 'meals/edit_reserve.html', context)


def delete_reserve(request, meal_id):
    reservation = Reserve.objects.get(id=meal_id)
    reservation.delete()
    return redirect("view_reserve")


# def edit_reserve(request):
#     reservation = Reserve.objects.get(Reserve)
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
