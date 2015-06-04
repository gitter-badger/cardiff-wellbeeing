from django.db import models
from django.contrib.auth.models import User


class Timeslot(models.Model):
    assignee = models.ForeignKey(User, verbose_name="assignee")
    start_time = models.DateTimeField("start")
    end_time = models.DateTimeField("end")
    session_type = models.ForeignKey(
        'SessionType', verbose_name="session type")

    class Meta:
        verbose_name = "time slot"
        verbose_name_plural = "time slots"


class SessionType(models.Model):
    name = models.CharField("name", unique=True, max_length=100)
    specialists = models.ManyToManyField(
        "User", related_name="session_types", blank=True)

    class Meta:
        verbose_name = "session type"
        verbose_name_plural = "session types"


class Client(models.Model):
    name = models.CharField("person's name", max_length=255)
    student_id = models.CharField("student ID", max_length=50)
    phone_number = models.CharField("phone number", max_length=25, blank=True)


class Appointment(models.Model):
    name = models.CharField("person's name", max_length=255)
    details = models.TextField("details", blank=True)
    client = models.ForeignKey("Client", blank=True, verbose_name="client")
    creation_date = models.DateTimeField("creation date", auto_now_add=True)
    modification_date = models.DateTimeField(
        "last modified", auto_now_add=True, auto_now=True)
    audit_notes = models.TextField("audit notes")
    timeslot = models.OneToOneField(
        'Timeslot', verbose_name="assigned time",
        related_name="appointment")

    class Meta:
        verbose_name = "request"
        verbose_name_plural = "requests"
