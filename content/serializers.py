from rest_framework import serializers

from content.models import Content


class ContentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="email", read_only=True)

    class Meta:
        model = Content
        fields = (
            "title",
            "content",
            "created_at",
            "updated_at",
            "author",
        )
        read_only_fields = ["author"]
