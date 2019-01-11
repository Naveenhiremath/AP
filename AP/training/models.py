from django.db import models
import uuid

# Create your models here.
"""
POSITION_CHOICES = (
    ('Fresher', 'Fresher'),
    ('SoftwareDeveloper', 'SD'),
    ('TechnicalAssocoiate', 'TA'),
    ('HumanResource', 'HR')
)


class Employee(models.Model):
    empid = models.IntegerField()
    name = models.CharField(max_length=15)
    designation = models.CharField(
        choices=POSITION_CHOICES,
        default="Fresher", max_length=15)

    def __str__(self):
        return self.name


class SecurityTraining(models.Model):
    video_id = models.IntegerField()
    name = models.CharField(max_length=15)
    added_at = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(default='default.png',blank=True)

    def __str__(self):
        return self.name


class ProfessionalBehaviour(models.Model):
    provideo_id = models.IntegerField()
    name = models.CharField(max_length=15)
    added_at = models.DateTimeField(auto_now_add=True)
    message = models.TextField(max_length=250)
    thumb = models.ImageField(default='default.png',blank=True)

    def __str__(self):
        return self.name
"""


class Event(models.Model):
    # uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=250)
    event_timestamp = models.DateTimeField(blank=True, null=True,auto_now_add=True)
    description = models.CharField(max_length=100,blank=True, null=True)


    # description = models.CharField(max_length=100,blank=True, null=True)
    # event_timestamp = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    # event_id = models.IntegerField()


def __str__(self):
    return self.name

