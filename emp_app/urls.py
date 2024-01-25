from django.urls import path, include
from . import views
urlpatterns = [
    path("", views.index , name= 'index'),
    path("view_all/", views.all_emp, name='all_emp'),
    path("add_emp/", views.add_empl, name='add_empl'),
    path("remove_emp/", views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>', views.remove_emp, name='remove_emp'),
    path("filter_emp/", views.filter_emp, name='filter_emp'),

]