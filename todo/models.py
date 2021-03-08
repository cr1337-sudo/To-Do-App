from django.db import models
from django.utils import timezone

# Create your models here.


class Todo(models.Model):
    UNINITIATED = "UNINITIATED" 
    IN_PROCESS="IN PROCESS"
    READY = "READY"
    STATUS=[
        (UNINITIATED,"UNINITIATED"),    
        (IN_PROCESS, "IN PROCESS"),
        (READY, "READY")
    ]
    task = models.CharField(max_length=200, blank = False, null=False)
    date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    state = models.CharField(max_length=100, choices=STATUS)


    def __str__(self):
        #return("TASK: %s | STATE: %s" %(self.task, self.state))
        return self.task