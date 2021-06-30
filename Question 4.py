totalMonths = 0
totalRainfall = 0
numberOfYears = int (input( "Please enter the number of years: "))
for currentYear in range (1, numberOfYears + 1):
    for currentMonth in range ( 1, 13):
        monthlyRain = float(input( "Please enter how many inches of rain there was for month " + format( currentMonth, "d" ) + ": ") )
        totalRainfall += monthlyRain
        totalMonths += 1
averageRainfall = totalRainfall / totalMonths
print( "Number of months: " ,totalMonths,)
print( "The total inces of rainfall is: ",totalRainfall)
print( "The average rainfall is: ",averageRainfall)


