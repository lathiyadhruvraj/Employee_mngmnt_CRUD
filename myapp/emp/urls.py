from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('home/', emp_home),
    path('add_emp/', add_emp),
    path('del_emp/<int:emp_id>/', del_emp),
    path('update_emp/<int:emp_id>/', update_emp),
    path('do_update/<int:emp_id>', do_update),

]
