from inspect import trace
from rest_framework import serializers
from . models import Student ,Track
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('fname','lname','age','student_track')
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Track
        fields=('track_name',)
       