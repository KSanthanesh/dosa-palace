from . import views
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('get_meal_list/', views.get_meal_list, name='get_meal_list'),
    path('get_meal_detail/<int:m_id>', views.get_meal_detail, name='get_meal_detail'),  # noqa: E501
    path('contact/', views.contact, name='contact'),
    path('reserve/', views.reserve, name='reserve'),
]
