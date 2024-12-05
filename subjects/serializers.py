from rest_framework import serializers
from .models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ["id", "name", "type", "created_at", "updated_at"]
