#The Fillup class represents one single visit to the gas station.
#Each time a driver fills their tank, they record three pieces of information:
#the odometer reading on the dashboard, how many gallons of fuel went in,
#and how much they paid for each gallon. This class stores those three
#numbers together and knows how to do the math on them.

#Bringing in the dataclass tool, which writes the __init__ method for us.
from dataclasses import dataclass


#The @dataclass line builds a new fill-up record from the three fields listed
#below, in that order: Fillup(odometer, gallons, pricePerGallon). Each value
#is saved inside the object so it can be read later, for example
#fillup.odometer or fillup.gallons.
@dataclass
class Fillup:
    odometer: float
    gallons: float
    pricePerGallon: float

    #The getCost method figures out the total dollars spent at the pump
    #by multiplying the gallons pumped by the price of each gallon.
    def getCost(self):
        return self.gallons * self.pricePerGallon

    #The milesSince method measures the distance driven since the previous
    #fill-up. It does this by subtracting the older odometer reading from
    #this one. For example, going from 30,000 miles to 30,300 miles means
    #the driver traveled 300 miles on that tank of gas.
    def milesSince(self, previousFillup):
        return self.odometer - previousFillup.odometer

    #The milesPerGallon method calculates the fuel efficiency for this tank.
    #It takes the miles driven since the last fill-up and divides that by the
    #gallons it took to refill the tank. A higher number means better mileage.
    #If no gallons were recorded, the method returns 0 so the program never
    #tries to divide by zero, which would crash it.
    def milesPerGallon(self, previousFillup):
        if self.gallons <= 0:
            return 0
        return self.milesSince(previousFillup) / self.gallons

    #The __str__ method describes this fill-up as a single readable line of
    #text, showing the odometer reading, the gallons, and the total cost.
    def __str__(self):
        return "Odometer %.1f | %.3f gallons | $%.2f spent" % \
               (self.odometer, self.gallons, self.getCost())
