from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup),
    path('login', views.login),
    path('test_token', views.test_token),
    path('logout', views.logout),
    path('notes', views.notes_view),
    path('notes/<int:pk>', views.user_notes),
    path('note', views.insert_note)
]
