from rest_framework import serializers
from task_tracker.models.comment import Comment

class CommentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=256)
    photo = serializers.ImageField()
    specs = serializers.FileField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.specs = validated_data.get('specs', instance.specs)
        return instance

    def save(self, validated_data):
        comment = self.create(validated_data)
        comment.save()