from rest_framework import serializers
from .models import data, region, impact, severeImpact

class dataSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField(many = True)
    class Meta:
        model = data
        fields = ['region', 'periodType', 'timeToElapse', 'reportedCases', 'population', 'totalHospitalBeds']

class impactSerializer(serializers.ModelSerializer):
    class Meta:
        model = impact
        fields = ['infectionByRequestedTime', 'severeCasesByRequestedTime', 'hospitalBedsByRequestedTime', 'casesForICUByRequestedTime', 'casesForVentilatorsByRequestedTime', 'dollarsInFlight']

class severeImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = severeImpact
        fields = ['infectionByRequestedTime', 'severeCasesByRequestedTime', 'hospitalBedsByRequestedTime', 'casesForICUByRequestedTime', 'casesForVentilatorsByRequestedTime', 'dollarsInFlight']