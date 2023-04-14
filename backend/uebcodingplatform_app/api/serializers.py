from rest_framework import serializers

class DummySerializer(serializers.Serializer):
    complexity = serializers.ChoiceField(
            required=True,
            choices=[
                'constant',
                'logarithmic'
                'linear',
                'linearithmic',
                'quadratic',
                'cubic',
                'polinomial'
            ])
    file = serializers.FileField(required=False)
    function = serializers.CharField(required=False, max_length=200)
    input = serializers.CharField(required=False, max_length=200)
    output = serializers.CharField(required=False, max_length=200)
    time = serializers.FloatField(required=False)

