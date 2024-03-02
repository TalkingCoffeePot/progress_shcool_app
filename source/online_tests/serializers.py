from rest_framework import serializers

from .models import Test, Question, Answer, UserAnswer, UserTest


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'is_correct', 'answer_text', 'answer_image']


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'question_name', 'question_text', 'question_image', 'answers', 'answer_count']


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ['id', 'test_name', 'difficulty', 'test_type', 'questions']


