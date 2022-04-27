from dataclasses import field
from django.contrib import admin
from .models import Track, Student
# Register your models here.

class CustomStudent(admin.ModelAdmin):
    fieldsets=(
        ['Student Info', {'fields': ('fname', 'lname', 'age')}],
        ['Scolarship info', {'fields': ('student_track',)}],
    )
    list_display = ('fname', 'lname', 'age', 'student_track', 'is_adult')
    list_filter = ( 'age', 'student_track__name')
    search_fields = ('fname', 'lname', 'age', 'student_track__name')

class InlineTrack(admin.TabularInline):
    model = Student
    extra = 1

class CustomTrack(admin.ModelAdmin):
    inlines = [InlineTrack]

admin.site.register(Track,CustomTrack)
admin.site.register(Student, CustomStudent)