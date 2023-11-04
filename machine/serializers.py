from rest_framework import serializers

from .models import Machine, Report, History


class MachineSerializer(serializers.ModelSerializer):
  class Meta:
    model = Machine
    fields = ['id', 'name']


class HistorySerializer(serializers.ModelSerializer):
  class Meta:
    model = History
    fields = ['status', 'timestamp', 'comment']


class ReportSerializer(serializers.ModelSerializer):
  # https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
  history = HistorySerializer(many=True)

  class Meta:
    model = Report
    fields = ['id', 'machine_id', 'issue',
              'description', 'timestamp', 'status', 'history']
