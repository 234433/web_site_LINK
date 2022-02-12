from django.urls import path

from .views import IndexView, AboutView

app_name = 'LINK'

urlpatterns = [
    path('', IndexView.as_view()),
    path('about/', AboutView.as_view()),
]
