from django.core.management.base import BaseCommand
from machine.models import Machine, Report


class Command(BaseCommand):
  help = 'Creates mockup data for the Machine API'

  def handle(self, *args, **options):
    machines = [
      {'id': 123, 'name': 'Machine 123'},
      {'id': 456, 'name': 'Machine 456'},
      {'id': 789, 'name': 'Machine 789'},
    ]

    reports = [
        {
            "id": 1,
            "machine_id": 123,
            "issue": "Overheating",
            "description": "The machine is overheating after running for an extended period.",
            "status": "Closed"
        },
        {
            "id": 2,
            "machine_id": 456,
            "issue": "Connection Failure",
            "description": "The machine is unable to establish a stable network connection.",
            "status": "Open"
        },
        {
            "id": 3,
            "machine_id": 123,
            "issue": "Strange Noises",
            "description": "Unusual noises are coming from the machine during operation.",
            "status": "Open"
        },
        {
            "id": 4,
            "machine_id": 789,
            "issue": "Software Crash",
            "description": "The machine's software is crashing when a specific task is executed.",
            "status": "Open"
        },
        {
            "id": 5,
            "machine_id": 789,
            "issue": "Critical System Failure",
            "description": "The machine's critical system has failed unexpectedly.",
            "status": "Urgent"
        }
    ]

    for machine in machines:
      Machine.objects.create(**machine)

    for report in reports:
      report['machine_id'] = Machine.objects.get(pk=report['machine_id'])
      Report.objects.create(**report)
