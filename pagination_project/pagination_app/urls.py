from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_student),
    path('display/', views.display_student),
    path('student/',views.StudentView.as_view()),
    path('add/',views.AddStudent.as_view()),
    path('get/<int:id>',views.GetStudent.as_view())
]
