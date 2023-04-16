from rest_framework import serializers

class DummySerializer(serializers.Serializer):
    file = serializers.FileField(required=True)
    time = serializers.FloatField(required=False, default=0)
    input = serializers.CharField(required=False, max_length=200, default="")
    complexity = serializers.ChoiceField(
        choices=["constant", "logarithmic", "linear", "linearithmic", "quadratic", "cubic", "polynomial"],
        required=False,
        default=""
    )
    function = serializers.CharField(required=False, max_length=200, default="")
    output = serializers.CharField(required=False, max_length=200, default="")
