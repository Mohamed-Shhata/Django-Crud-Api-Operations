from rest_framework import serializers
from .models import Student,Track

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    # def to_representation(self, instance):
    #     ret = super().to_representation(instance)
    #     ret['student_track'] = instance.student_track.name
    #     return ret
        
 
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'