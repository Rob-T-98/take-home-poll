from django.db import models

class Answers(models.Model):
    q1Choices = (
        ('none','None Selected'),
        ('Front', 'Frontend'),
        ('Back', 'Backend'),
        ('Both','Both'),
    )
    q2Choices = (
        ('none','None Selected'),
        ('0','0'),
        ('1-2','1-2'),
        ('3-4','3-4'),
        ('5-6','5-6'),
        ('7+','7+'),
    )
    q3Choices = (
        ('none','None Selected'),
        ('pg','PostgreSQL'),
        ('my','MySQL'),
        ('o','Oracle'),
        ('sqls','SQL Server'),
    )
    stack=models.CharField(max_length=20,choices=q1Choices,default="none")
    exp=models.CharField(max_length=20,choices=q2Choices,default="none")
    years=models.IntegerField()
    db=models.CharField(max_length=20,choices=q3Choices,default="none")

# Create your models here.
