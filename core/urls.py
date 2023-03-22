from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from core import views

urlpatterns = [
    path('core/', views.BookListCreate.as_view()),
    path('core/<int:pk>', views.BookDetail.as_view()),
    path('core/book-edit-delete/<int:pk>', views.BookEditDelete.as_view()),
    path('core/tracker', views.TrackerListCreate.as_view()),
    path('core/tracker-edit-delete/<int:pk>',
         views.TrackerEditDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
