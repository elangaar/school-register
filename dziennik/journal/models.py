from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    position = models.ForeignKey('Position')
    which_class = models.ForeignKey('Class_', null=True, blank=True, default=True)

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Position(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Class_(models.Model):
    level = models.PositiveIntegerField()
    branch = models.CharField(max_length=1)
    classroom = models.ForeignKey('Classroom', null=True)
    school = models.ForeignKey('School', null=True)

    def __str__(self):
        return "{0}{1}".format(self.level, self.branch)


class Classroom(models.Model):
    number = models.PositiveIntegerField()

    def __str__(self):
        return "{0}".format(self.number)


class School(models.Model):
    PRZEDSZKOLE = "Przedszkole"
    ZEROWKA = "Zerowka"
    PODSTAWOWA = "Podstawowa"
    SREDNIA = "Srednia"
    TYPES_OF_SCHOOLS_CHOICES = (
        (PRZEDSZKOLE, "Przedszkole"),
        (ZEROWKA, "Zerowka"),
        (PODSTAWOWA, "Podstawowa"),
        (SREDNIA, "Srednia"),
    )
    type_of_school = models.CharField(
        max_length=20,
        choices=TYPES_OF_SCHOOLS_CHOICES,
    )
    name = models.CharField(max_length=50)

    def __str__(self):
        return "{0}".format(self.name)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    classroom = models.ForeignKey('Classroom', null=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pesel = models.BigIntegerField()
    which_class = models.ForeignKey('Class_')
    degrees = models.ManyToManyField('Degree', null=True, blank=True,
    related_name='student')
    notes = models.ForeignKey('Note', null=True, blank=True)
    parents = models.ForeignKey('Parent')

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)


class Degree(models.Model):
    value = models.PositiveIntegerField()
    category = models.CharField(max_length=20)
    subject = models.ForeignKey('Subject')

    def __str__(self):
        return "{0} {1}".format(self.value, self.category)


class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    def __str__(self):
        return "{0}".format(self.title)


class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone_number = models.BigIntegerField()


    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

