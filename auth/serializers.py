from rest_framework import serializers

class CardSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=120)
	desc = serializers.CharField()