from rest_framework import serializers

class DummySerializer(serializers.Serializer):
    file = serializers.FileField()
    input = serializers.CharField()
    complexity = serializers.ChoiceField(
            choices=['LogN', 'NLogN', 'N*N'])
    function = serializers.CharField(max_length=200)
