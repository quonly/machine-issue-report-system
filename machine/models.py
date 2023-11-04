from django.db import models


class Machine(models.Model):
  name = models.CharField(max_length=255)

  def __str__(self):
    return f'{self.pk}: {self.name}'

  def get_count_report(self):
    return self.report_set.count()


STATUS_CHOICES = (
    ('Open', 'Open'),
    ('Urgent', 'Urgent'),
    ('Closed', 'Closed'),
    ('Resolved', 'Resolved'),
  )


class Report(models.Model):
  machine_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
  issue = models.CharField(max_length=100)
  description = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)
  status = models.CharField(
    max_length=10, default='Open', choices=STATUS_CHOICES)

  def __str__(self):
    return f'{self.id}'


class History(models.Model):
  report_id = models.ForeignKey(
    Report, on_delete=models.CASCADE, related_name='history')
  status = models.CharField(
    max_length=10, default='Open', choices=STATUS_CHOICES)
  timestamp = models.DateTimeField(auto_now_add=True)
  comment = models.TextField(blank=True, null=True)

  def save(self, *args, **kwargs):
    # override save method for updating Report model status when History model have change
    report = self.report_id
    report.status = self.status
    report.save()
    super(History, self).save(*args, **kwargs)
