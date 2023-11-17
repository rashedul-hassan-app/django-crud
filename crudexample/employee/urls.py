from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('add/', views.employee_add_or_update, name='employee_add'),
    path('add/<int:id>', views.employee_add_or_update,
         name='employee_update'),
]

# www.site.com/employee/list
# www.site.com/employee/update/3
