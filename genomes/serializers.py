from rest_framework import serializers
from genomes.models import AssemblySummary, ANI_report_prokaryotes, Prokaryotes

class AssemblySummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = AssemblySummary
        fields = '__all__'


class ANISerializer(serializers.ModelSerializer):

    class Meta:
        model = ANI_report_prokaryotes
        fields = '__all__'

class ProkaryotesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prokaryotes
        fields = '__all__'

class AssemblyTaxonomySerializer(serializers.Serializer):
    rsync = serializers.CharField()
    sub = serializers.CharField(max_length=255)
    