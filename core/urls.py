from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('core/', views.BookList.as_view()),
    path('core/<int:pk>', views.BookDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
