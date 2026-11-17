#The FuelLog class is the collection that holds every fill-up for one vehicle.
#A single Fillup only knows about itself, so something has to hold them all in
#order and compare them to each other. That is the job of this class. It keeps
#the fill-ups in a list and answers questions such as "what is my average gas
#mileage" and "which tank was my worst."

class FuelLog:

    #The __init__ method creates a brand new, empty log for one vehicle.
    #It saves the vehicle's nickname and starts an empty list that fill-ups
    #will be added into as the user enters them.
    def __init__(self, vehicleName):
        self.vehicleName = vehicleName
        self.fillups = []

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
    #tank of fuel. It pairs each fill-up with the one directly before it and
    #compares the two. The first fill-up is skipped on purpose because there
    #is nothing earlier to compare it against, so self.fillups[1:] starts the
    #"current" side of each pair at the second fill-up.
    def getMpgList(self):
        return [current.milesPerGallon(previous)
                for previous, current in zip(self.fillups, self.fillups[1:])]

    #The getTotalMiles method reports the total distance covered across the
    #whole log by subtracting the very first odometer reading from the last one.
    #If there is not enough data yet, it reports zero miles.
    def getTotalMiles(self):
        if not self.hasEnoughData():
            return 0
        return self.fillups[-1].milesSince(self.fillups[0])

    #The getTotalCost method adds up the dollars spent on every fill-up after
    #the first one. The first fill-up is left out of the total on purpose: the
    #program has no way of knowing how far the driver traveled on that very
    #first tank, so counting its cost would unfairly inflate the cost per mile.
    def getTotalCost(self):
        return sum(fillup.getCost() for fillup in self.fillups[1:])

    #The getAverageMpg method reports the typical gas mileage across the log.
    #Rather than averaging the individual tank averages, it divides the total
    #miles traveled by the total gallons burned, which is the more accurate way
    #to combine tanks of different sizes. With fewer than two fill-ups there
    #are no gallons to count, so it reports zero instead of dividing by zero.
    def getAverageMpg(self):
        totalGallons = sum(fillup.gallons for fillup in self.fillups[1:])
        if totalGallons <= 0:
            return 0
        return self.getTotalMiles() / totalGallons

    #The getBestMpg method finds the single most fuel-efficient tank in the log.
    #It reports zero when there are no tanks to compare yet.
    def getBestMpg(self):
        return max(self.getMpgList(), default=0)

    #The getWorstMpg method finds the single least fuel-efficient tank.
    def getWorstMpg(self):
        return min(self.getMpgList(), default=0)

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

    #The getSummaryLines method lists the combined statistics for the whole
    #log as lines of text. The report on the screen and the report saved to
    #the file show the same numbers, so both ask this one method for them.
    #The "unit" is how mileage should be labeled, for example "MPG".
    def getSummaryLines(self, unit):
        return [
            "Total miles driven: %.1f" % self.getTotalMiles(),
            "Total spent on fuel: $%.2f" % self.getTotalCost(),
            "Average mileage: %.2f %s" % (self.getAverageMpg(), unit),
            "Best tank: %.2f %s" % (self.getBestMpg(), unit),
            "Worst tank: %.2f %s" % (self.getWorstMpg(), unit),
            "Fuel cost per mile: $%.3f" % self.getCostPerMile(),
        ]

    #The __str__ method describes the log in one short readable line.
    def __str__(self):
        return "Fuel log for %s with %d fill-up(s) recorded" % \
               (self.vehicleName, self.getCount())
