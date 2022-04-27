from django.db import models

# Create your models here.
class Track(models.Model):
    name = models.CharField(max_length=100)
    # description = models.TextField(blank=True)
    # url = models.URLField(blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    fname = models.CharField(max_length=100, null=True)
    lname = models.CharField(max_length=100, default='' )
    age = models.IntegerField()
    student_track = models.ForeignKey(Track, on_delete=models.CASCADE)
    
    # email = models.EmailField()
    # address = models.CharField(max_length=200)
    # phone = models.CharField(max_length=20)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.fname + ' ' + self.lname

    def is_adult(self):
        return self.age >= 22

    is_adult.short_description = 'Graduation Student'
    is_adult.boolean = True