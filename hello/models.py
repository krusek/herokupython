from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Project(models.Model):
  name = models.CharField(max_length=100)
  
BACKLOG = "BL"
IN_PROGRESS = "IP"
IN_REVIEW = "IR"
DONE = "DN"
STATUS_CHOICES = (
  (BACKLOG, "Backlog"),
  (IN_PROGRESS, "In Progress"),
  (IN_REVIEW, "In Review"),
  (DONE, "Done"),
)

class Ticket(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  project = models.ForeignKey(Project, on_delete=models.CASCADE)
  
  status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=BACKLOG)
  
class TicketTime(models.Model):
  start = models.DateTimeField('clock-in', auto_now_add=True)
  stop = models.DateTimeField('clock-out', null=True)
  status = models.CharField(max_length=2, choices=STATUS_CHOICES, default=BACKLOG)
  ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)