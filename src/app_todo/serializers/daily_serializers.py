from rest_framework import serializers
from core.models import (
    TodoDaily,
    UserTodo,
)


class DailySerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoDaily
        fields = [
            'id',
            'name',
            'description',
            'done_at',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id', 'done_at', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        user_todo, _ = UserTodo.objects.get_or_create(user=user)
        todo_daily = TodoDaily.objects.create(
            user_todo=user_todo,
            **validated_data)
        return todo_daily

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance

class RequestTodoDailyDoneStatusSerializer(serializers.Serializer):
    is_done = serializers.BooleanField(required=True)