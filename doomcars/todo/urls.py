from django.urls import path
from .import views
from django.contrib.auth .views import LoginView,LogoutView
urlpatterns = [
    path('',views.home,name='all-notes'),
    path('note/<str:noteid>',views.noteView,name='note'),
    path('notes/',views.allNotes,name='user-notes'),
    path('create/',views.createnote,name='create'),
    path('login/',LoginView.as_view(template_name='todo/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='todo/logout.html'),name='logout')
]
