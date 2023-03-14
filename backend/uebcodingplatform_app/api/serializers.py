from rest_framework import serializers

class DummySerializer(serializers.Serializer):
    complexity = serializers.ChoiceField(
            choices=[
                'constant', 
                'logarithmic', 
                'linear',
                'Nlogarithmic',
                'quadratic',
                'cubic',
                'polynomial'
            ])
    file = serializers.FileField()
    function = serializers.CharField(max_length=200)
    input = serializers.CharField(max_length=200)
    output = serializers.CharField(max_length=200)
    time = serializers.FloatField()

