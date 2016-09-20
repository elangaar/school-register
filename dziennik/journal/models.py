from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pesel = models.BigIntegerField()
    position = models.ForeignKey('Position')
    which_class = models.ForeignKey('Class_', null=True, blank=True, default=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0} {1}".format(self.last_name, self.first_name)


class Position(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Class_(models.Model):
    level = models.PositiveIntegerField()
    branch = models.CharField(max_length=1)
    classroom = models.ForeignKey('Classroom', null=True)
    school = models.ForeignKey('School', null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0}{1}".format(self.level, self.branch)

#    def get_absolute_url(self):
#        return "{1}".format(self.slug,)


class Classroom(models.Model):
    number = models.PositiveIntegerField()
    slug = models.SlugField(unique=True)

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
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0}".format(self.name)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    classroom = models.ManyToManyField('Classroom')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    pesel = models.BigIntegerField()
    which_class = models.ForeignKey('Class_')
    grades = models.ManyToManyField('Grade',
    related_name='student')
    notes = models.ManyToManyField('Note')
    parents = models.ManyToManyField('Parent')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0} {1}".format(self.last_name, self.first_name)


class Grade(models.Model):
    value = models.PositiveIntegerField()
    category = models.CharField(max_length=20)
    subject = models.ForeignKey('Subject')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0} {1}".format(self.value, self.category)


class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0}".format(self.title)

class Parent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    telephone_number = models.BigIntegerField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return "{0} {1}".format(self.last_name, self.first_name)


def create_slug_position(instance):
    slug = slugify("%s" % (instance.name, ))
    return slug

def create_slug_class_(instance):
    slug = slugify("%s-%s" % (instance.level, instance.branch))
    return slug

def create_slug_school(instance):
    slug = slugify("%s" % (instance.name, ))
    return slug

def create_slug_classroom(instance):
    slug = slugify("%s" % (instance.number, ))
    return slug

def create_slug_subject(instance):
    slug = slugify("%s" % (instance.name, ))
    return slug

def create_slug_grade(instance):
    slug = slugify("%s" % (instance.value, ))
    return slug

def create_slug_employee(instance, new_slug=None):
    slug = slugify("%s-%s" % (instance.last_name, instance.first_name))
    if new_slug is not None:
        slug = new_slug
    qs = Employee.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s-%s" % (instance.last_name, instance.first_name, qs.first().id)
        return create_slug_employee(instance, new_slug=new_slug)
    return slug

def create_slug_student(instance, new_slug=None):
    slug = slugify("%s-%s" % (instance.last_name, instance.first_name))
    if new_slug is not None:
        slug = new_slug
    qs = Student.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s-%s" % (instance.last_name, instance.first_name, qs.first().id)
        return create_slug_student(instance, new_slug=new_slug)
    return slug

def create_slug_note(instance, new_slug=None):
    slug = slugify("%s" % (instance.title))
    return slug

def create_slug_parent(instance, new_slug=None):
    slug = slugify("%s-%s" % (instance.last_name, instance.first_name))
    if new_slug is not None:
        slug = new_slug
    qs = Parent.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s-%s" % (instance.last_name, instance.first_name, qs.first().id)
        return create_slug_employee(instance, new_slug=new_slug)
    return slug

def pre_save_employee_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_employee(instance)

def pre_save_student_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_student(instance)

def pre_save_parent_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_employee_student_parent(instance)

def pre_save_note_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_note(instance)

def pre_save_position_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_position(instance)

def pre_save_class__receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_class_(instance)

def pre_save_school_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_school(instance)

def pre_save_classroom_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_classroom(instance)

def pre_save_subject_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_subject(instance)

def pre_save_grade_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug_grade(instance)

pre_save.connect(pre_save_employee_receiver, sender=Employee)
pre_save.connect(pre_save_student_receiver, sender=Student)
pre_save.connect(pre_save_parent_receiver, sender=Parent)
pre_save.connect(pre_save_note_receiver, sender=Note)
pre_save.connect(pre_save_position_receiver, sender=Position)
pre_save.connect(pre_save_class__receiver, sender=Class_)
pre_save.connect(pre_save_school_receiver, sender=School)
pre_save.connect(pre_save_classroom_receiver, sender=Classroom)
pre_save.connect(pre_save_subject_receiver, sender=Subject)
pre_save.connect(pre_save_grade_receiver, sender=Grade)
