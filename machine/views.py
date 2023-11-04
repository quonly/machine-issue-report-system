from rest_framework import generics
from django_filters import rest_framework as filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Count

from .models import Machine, Report
from .serializers import MachineSerializer, ReportSerializer


class MachineAPIView(generics.ListCreateAPIView):
  queryset = Machine.objects.all()
  serializer_class = MachineSerializer


class ReportFilter(filters.FilterSet):
  '''
  Example query parameter

  ?machine_id=123&title=Overheating&start_timestamp=2023-08-01&end_timestamp=2023-12-26&status=Closed
  '''
  title = filters.CharFilter(field_name='issue', lookup_expr='icontains')
  start_timestamp = filters.DateTimeFilter(
    field_name='timestamp', lookup_expr='gt')
  end_timestamp = filters.DateTimeFilter(
    field_name='timestamp', lookup_expr='lt')

  class Meta:
    model = Report
    fields = ['machine_id', 'issue', 'timestamp', 'status']


class ReportAPIView(generics.ListCreateAPIView):
  queryset = Report.objects.all()
  serializer_class = ReportSerializer
  filterset_class = ReportFilter


class ReportDetailAPIView(generics.RetrieveUpdateAPIView):
  queryset = Report.objects.all()
  serializer_class = ReportSerializer


@api_view()
def report_per_machine(request):
  machines = Machine.objects.annotate(num_report=Count('machine'))
  data = []
  for m in machines:
    data.append({'machine_id': m.id, 'issue_count': m.num_report})
  return Response(data)
