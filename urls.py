from os import link
from django.urls import path

from .views import IndexView, AboutView

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
]
app_name = 'LINK'
urlpatterns = 