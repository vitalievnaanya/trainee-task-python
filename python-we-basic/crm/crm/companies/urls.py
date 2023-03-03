from django.urls import path
from .views import CompanyListCreateAPIView,\
    CompanyRetrieveUpdateDestroyAPIView, \
    EmployeeListCreateAPIView,\
    EmployeeRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', CompanyListCreateAPIView.as_view()),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyAPIView.as_view())
]