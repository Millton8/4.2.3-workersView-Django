
from django.contrib import admin
from django.urls import path
from viewWorkers import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('generalreport/', views.rezofwork),
    path('workerlist/', views.workerlist),
    path('workerlist/edit/<int:id>', views.edit),
    path('workerlist/delete/<int:id>', views.delete),
    path('accounts/login/', views.myview),
    path('register/', views.register),
    path('login/', views.myview),
]
