from rest_framework import serializers

class DummySerializer(serializers.Serializer):
    file = serializers.FileField()
    time = serializers.FloatField()
    input = serializers.CharField(max_length=200)
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
    function = serializers.CharField(max_length=200)
