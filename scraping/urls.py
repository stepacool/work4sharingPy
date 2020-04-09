from django.urls import path

from scraping.views import CreateEmployeeView

urlpatterns = [
    path('employees/', CreateEmployeeView.as_view())
]