from rest_framework import serializers

from .models import Test, TestQuestion, TestQuestionAnswer, Category


class TestQuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestQuestionAnswer
        fields = "__all__"


class TestQuestionSerializer(serializers.ModelSerializer):
    answers = TestQuestionAnswerSerializer()
    class Meta:
        model = TestQuestion
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    # questions = TestQuestionSerializer(many=True)
    class Meta:
        model = Test
        fields = "__all__"

class CategorySerializer(serializer.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
