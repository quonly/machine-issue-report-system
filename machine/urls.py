from django.urls import path
from . import views

urlpatterns = [
  path('v1/machine/', views.MachineAPIView.as_view(), name='machine_list'),
  path('v1/machine/num-report/', views.MachineAPIView.as_view(), name='num_report'),
  path('v1/report/', views.ReportAPIView.as_view(), name='report_list'),
  path('v1/report/<int:pk>/', views.ReportDetailAPIView.as_view(), name='report_list'),
]
