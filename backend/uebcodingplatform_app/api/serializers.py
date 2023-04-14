from rest_framework import serializers


class DummySerializer(serializers.Serializer):
    file = serializers.FileField(required=True)
    time = serializers.FloatField(required=False)
    input = serializers.CharField(required=False, max_length=200)
    complexity = serializers.ChoiceField(
        choices=[
            'constant',
            'logarithmic',
            'linear',
            'Nlogarithmic',
            'quadratic',
            'cubic',
            'polynomial'
        ], required=False)
    function = serializers.CharField(max_length=200, required=False)
