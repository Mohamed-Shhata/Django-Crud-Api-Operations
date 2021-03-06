from django.urls import path,include
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    path('show/<student_id>',views.show,name='show'),
    path("delete/<student_id>",views.delete,name='delete'),
    path('add/',views.add_student,name='add'),
    path('edit/<student_id>',views.editStudent,name='edit'),

     #rest_framework api urls
    path('api-all/', views.api_all_student, name='api-all'),
    path('api-add/', views.api_add_student, name='api-add'),
    path('api-edit/<std_id>', views.api_edit_student, name='api-edit'),
    path('api-one/<std_id>', views.api_one_student, name='api-one'),
    path('api-delete/<std_id>', views.api_delete_student, name='api-delete'),
    path('api-auth/', include('rest_framework.urls')),

    # auth urls
    path('login/', views.signIn , name='login'),
    path('signup/', views.signUp , name='signup'),
    path('signout/', views.signOut , name='signout')
    
]
