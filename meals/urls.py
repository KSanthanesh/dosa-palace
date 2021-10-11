from . import views
from django.urls import path
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('get_meal_list/', views.get_meal_list, name='get_meal_list'),
    path('get_meal_detail/<int:m_id>', views.get_meal_detail, name='get_meal_detail'),  # noqa: E501
    path('contact/', views.contact, name='contact'),
    path('contact_reply/', views.contact_reply, name='contact_reply'),
    path('add_reserve/', views.add_reserve, name='add_reserve'),
    path('view_reserve/', views.view_reserve, name='view_reserve'),
    path('edit/<meal_id>', views.edit_reserve, name='edit'),
    path('delete/<meal_id>', views.delete_reserve, name='delete'),
    path('user_list/', views.user_list, name='user_list'),
]
