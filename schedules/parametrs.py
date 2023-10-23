from django.db import models


class ScheduleParameters(models.Model):
    title = models.CharField(max_length=255)
    work_days = models.PositiveIntegerField()
    off_days = models.PositiveIntegerField()

    def __str__(self):
        return self.title
