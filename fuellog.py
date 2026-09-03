#The FuelLog class is the collection that holds every fill-up for one vehicle.
#A single Fillup only knows about itself, so something has to hold them all in
#order and compare them to each other. That is the job of this class. It keeps
#the fill-ups in a list and answers questions such as "what is my average gas
#mileage" and "which tank was my worst."

#We need the Fillup class so this file understands what a fill-up is.
from fillup import Fillup

class FuelLog(object):

    #The __init__ method creates a brand new, empty log for one vehicle.
    #It saves the vehicle's nickname and starts an empty list that fill-ups
    #will be added into as the user enters them.
    def __init__(self, vehicleName):
        self.vehicleName = vehicleName
        self.fillups = []

    #The getVehicleName method hands back the nickname of the vehicle.
    def getVehicleName(self):
        return self.vehicleName

    #The addFillup method adds one new fill-up record to the end of the list.
    def addFillup(self, fillup):
        self.fillups.append(fillup)

    #The getCount method reports how many fill-ups have been entered so far.
    def getCount(self):
        return len(self.fillups)

    #The hasEnoughData method answers whether the program can calculate gas
    #mileage yet. Mileage is always measured BETWEEN two fill-ups, because the
    #program needs a starting odometer reading and an ending one. That means at
    #least two fill-ups must exist before any mileage math is possible.
    def hasEnoughData(self):
        return self.getCount() >= 2

    #The getMpgList method builds a list of the gas mileage figures for every
    #tank of fuel. It walks through the fill-ups starting at the second one,
    #and for each it compares that fill-up to the one directly before it.
    #The first fill-up is skipped on purpose because there is nothing earlier
    #to compare it against.
    def getMpgList(self):
        mpgList = []
        for index in range(1, self.getCount()):
            current = self.fillups[index]
            previous = self.fillups[index - 1]
            mpgList.append(current.milesPerGallon(previous))
        return mpgList

    #The getTotalMiles method reports the total distance covered across the
    #whole log by subtracting the very first odometer reading from the last one.
    #If there is not enough data yet, it reports zero miles.
    def getTotalMiles(self):
        if not self.hasEnoughData():
            return 0
        first = self.fillups[0]
        last = self.fillups[self.getCount() - 1]
        return last.milesSince(first)

    #The getTotalCost method adds up the dollars spent on every fill-up after
    #the first one. The first fill-up is left out of the total on purpose: the
    #program has no way of knowing how far the driver traveled on that very
    #first tank, so counting its cost would unfairly inflate the cost per mile.
    def getTotalCost(self):
        total = 0
        for index in range(1, self.getCount()):
            total += self.fillups[index].getCost()
        return total

    #The getAverageMpg method reports the typical gas mileage across the log.
    #Rather than averaging the individual tank averages, it divides the total
    #miles traveled by the total gallons burned, which is the more accurate way
    #to combine tanks of different sizes.
    def getAverageMpg(self):
        if not self.hasEnoughData():
            return 0
        totalGallons = 0
        for index in range(1, self.getCount()):
            totalGallons += self.fillups[index].getGallons()
        if totalGallons <= 0:
            return 0
        return self.getTotalMiles() / totalGallons

    #The getBestMpg method finds the single most fuel-efficient tank in the log.
    def getBestMpg(self):
        if not self.hasEnoughData():
            return 0
        return max(self.getMpgList())

    #The getWorstMpg method finds the single least fuel-efficient tank.
    def getWorstMpg(self):
        if not self.hasEnoughData():
            return 0
        return min(self.getMpgList())

    #The getCostPerMile method reports how many dollars the driver spends on
    #fuel for each mile traveled. It divides the total money spent by the total
    #miles driven. If no miles have been recorded, it returns zero so the
    #program never divides by zero.
    def getCostPerMile(self):
        if self.getTotalMiles() <= 0:
            return 0
        return self.getTotalCost() / self.getTotalMiles()

    #The estimateTripCost method predicts what fuel will cost for an upcoming
    #trip of a given distance. It multiplies the planned trip distance by the
    #driver's own historical cost per mile, so the estimate is based on how
    #this specific vehicle has actually been performing.
    def estimateTripCost(self, tripMiles):
        return tripMiles * self.getCostPerMile()

    #The __str__ method describes the log in one short readable line.
    def __str__(self):
        return "Fuel log for %s with %d fill-up(s) recorded" % \
               (self.vehicleName, self.getCount())
