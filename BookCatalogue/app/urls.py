from django.urls import path
from . import views

urlpatterns  = [
    path('book-data/',views.BookData.as_view(),name='get-data'),
]