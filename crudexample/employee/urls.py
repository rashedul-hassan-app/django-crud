from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.employee_list, name='employee_list'),
    path('add/', views.employee_add_or_update, name='employee_add'),
    path('update/<int:id>', views.employee_add_or_update,
         name='employee_update'),
    path('delete/<int:id>', views.employee_delete, name='employee_delete'),
]

# www.site.com/employee/list
# www.site.com/employee/update/3
