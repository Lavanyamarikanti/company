from django.urls import include, path
from . import views
urlpatterns = [
    path('',views.home),
    path('create/',views.create_student),
    path('add/',views.add_student),
    path('get/<int:id>',views.get_student),
    path('get_all/',views.get_all_students),
    path('delete/<int:id>',views.delete_student),
    path('update/<int:id>',views.update_student)
]
