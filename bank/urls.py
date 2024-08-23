from django.urls import path

from .views import percent_result

urlpatterns = [
    path('', percent_result),
]
