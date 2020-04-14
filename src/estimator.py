def estimator(data):
  
  impactCurrentlyInfected = int(data['reportedCases'] * 10)

  severeImpactCurrentlyInfected = int(data['reportedCases'] * 50)

  if data['periodType'] == 'days':
    normalDays = data['timeToElapse']
  elif data['periodType'] == 'weeks':
    normalDays = data['timeToElapse'] * 7
  elif data['periodType'] == 'months':
    normalDays = data['timeToElapse'] * 30
  else:
    normalDays = data['timeToElapse'] * 365   # Just in case there is a need to account for years
    
  impactInfectionsByRequestedTime = impactCurrentlyInfected * 2**int(normalDays / 3)
  severeImpactInfectionsByRequestedTime = severeImpactCurrentlyInfected * 2**int(normalDays / 3)

  impactSevereCasesByRequestedTime = int(0.15 * impactInfectionsByRequestedTime)

  severeImpactSevereCasesByRequestedTime = int(0.15 * severeImpactInfectionsByRequestedTime)

  availableBeds = int(0.35 * data['totalHospitalBeds']) # Estimated availability of beds per time is 35%

  if impactSevereCasesByRequestedTime <= availableBeds:
    impactHospitalBedsByRequestedTime = availableBeds
  else:
    impactHospitalBedsByRequestedTime = availableBeds - impactSevereCasesByRequestedTime

  if severeImpactSevereCasesByRequestedTime <= availableBeds:
    severeImpactHospitalBedsByRequestedTime = availableBeds
  else:
    severeImpactHospitalBedsByRequestedTime = availableBeds - severeImpactSevereCasesByRequestedTime

  impactCasesForICUByRequestedTime = int(0.05 * impactInfectionsByRequestedTime)

  severeImpactCasesForICUByRequestedTime = int(0.05 * severeImpactInfectionsByRequestedTime)

  impactCasesForVentilatorsByRequestedTime = int(0.02 * impactInfectionsByRequestedTime)

  severeImpactCasesForVentilatorsByRequestedTime = int(0.02 * severeImpactInfectionsByRequestedTime)

  impactDollarsInFlight = int(impactInfectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD'] / normalDays)

  severeImpactDollarsInFlight = int(severeImpactInfectionsByRequestedTime * data['region']['avgDailyIncomePopulation'] * data['region']['avgDailyIncomeInUSD'] / normalDays)


  impact = {'currentlyInfected': impactCurrentlyInfected,
          'infectionsByRequestedTime': impactInfectionsByRequestedTime,
          'severeCasesByRequestedTime': impactSevereCasesByRequestedTime,
          'hospitalBedsByRequestedTime': impactHospitalBedsByRequestedTime,
          'casesForICUByRequestedTime': impactCasesForICUByRequestedTime,
          'casesForVentilatorsByRequestedTime': impactCasesForVentilatorsByRequestedTime,
          'dollarsInFlight': impactDollarsInFlight

          }
  
  severeImpact = {'currentlyInfected': severeImpactCurrentlyInfected,
          'infectionsByRequestedTime': severeImpactInfectionsByRequestedTime,
          'severeCasesByRequestedTime': severeImpactSevereCasesByRequestedTime,
          'hospitalBedsByRequestedTime': severeImpactHospitalBedsByRequestedTime,
          'casesForICUByRequestedTime': severeImpactCasesForICUByRequestedTime,
          'casesForVentilatorsByRequestedTime': severeImpactCasesForVentilatorsByRequestedTime,
          'dollarsInFlight': severeImpactDollarsInFlight
          }

  estimate = {'data': data, 'impact': impact, 'severeImpact': severeImpact}
  
  return estimate
