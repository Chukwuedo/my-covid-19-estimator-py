from django.db import models

class data(models.Model):
    periodType = models.CharField(max_length = 50)
    timeToElapse = models.DecimalField(max_digits=20, decimal_places=10)
    reportedCases = models.DecimalField(max_digits=20, decimal_places=10)
    population = models.DecimalField(max_digits=20, decimal_places=10)
    totalHospitalBeds = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.regionName

class region(models.Model):
    regionDetail = models.ForeignKey(data, related_name = 'region', on_delete = models.CASCADE)
    name = models.CharField(max_length = 50)
    avgAge = models.DecimalField(max_digits=20, decimal_places=10)
    avgDailyIncomeInUSD = models.DecimalField(max_digits=20, decimal_places=10)
    avgDailyIncomePopulation = models.DecimalField(max_digits=20, decimal_places=10)

    class Meta:
        ordering = ['name']

class impact(models.Model):
    infectionByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    severeCasesByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    hospitalBedsByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    casesForICUByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    casesForVentilatorsByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    dollarsInFlight = models.DecimalField(max_digits=20, decimal_places=1)

class severeImpact(models.Model):
    infectionByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    severeCasesByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    hospitalBedsByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    casesForICUByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    casesForVentilatorsByRequestedTime = models.DecimalField(max_digits=20, decimal_places=1)
    dollarsInFlight = models.DecimalField(max_digits=20, decimal_places=1)


