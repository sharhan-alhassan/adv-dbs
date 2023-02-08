from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

import uuid

# Create your models here.

"""
- Student(studentID, studentFirstName, studentLastName, studentGender, studentDob, )
Primary Key studentID

- Course(courseID, courseName, courseDescription, courseStartDate, courseEndDate)
Primary Key courseID

- ReportCard(reportID, studentID, courseID, marks, date)
Primary Key reportID
Foreign Key studentID reference Student
Foreign Key courseID reference Course

- Profile (profileID, studentID, studentAvator, studentFullName, studentAge)
Primary Key profileID
Foreign Key studentID references Student

- MealPlan (mealPlanID, student, cost)
Primary Key mealPlanID

"""

SEMESTER_COURSES = (
    ('None', 'None'),
    ('Data Structures', 'Data Structures'),
    ('Wireless Systems', 'Wireless Systems'),
    ('Advanced Databases', 'Advanced Databases'),
    ('Research Methods', 'Research Methods'),
    ('Advanced OS', 'Advanced OS')
)


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    gender = models.CharField(max_length=50, null=True, blank=True)
    dob = models.DateField()
    fullname = models.CharField(max_length=150, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname}-{self.lastname}"

    def get_absolute_url(self):
        return reverse("student-detail", args=[str(self.id)])


class Course(models.Model):
    course_name = models.CharField(max_length=150, choices=SEMESTER_COURSES, default='None')
    description = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.course_name


class ReportCard(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student}'s-report"


