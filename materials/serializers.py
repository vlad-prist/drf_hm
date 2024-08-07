from rest_framework import serializers

from materials.models import Course, Lesson
from materials.validators import validate_link


class LessonSerializer(serializers.ModelSerializer):
    link = serializers.URLField(validators=[validate_link])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lesson = LessonSerializer(source='lesson_set', many=True, read_only=True)
    link = serializers.URLField(validators=[validate_link])

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, obj):
        return obj.lesson_set.count()
