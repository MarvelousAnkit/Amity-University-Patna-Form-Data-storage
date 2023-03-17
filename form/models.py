from django.db import models


class Summary2(models.Model):
    Batch = models.CharField(max_length=100)
    Program = models.CharField(max_length=100)
    Semester = models.CharField(max_length=300)
    Course_Title = models.CharField(max_length=300)
    Course_Unit = models.CharField(max_length=100)
    Course_Level = models.CharField(max_length=100)
    Course_Code = models.CharField(max_length=100)
    Course_Objective = models.CharField(max_length=2000)
    Course_Content = models.CharField(max_length=100)
    Course_Weightage = models.CharField(max_length=100)
    Student_Learning_Outcome = models.CharField(max_length=3000)
    Pedagogy = models.CharField(max_length=2000)
