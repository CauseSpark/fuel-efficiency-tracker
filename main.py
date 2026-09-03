#FUEL EFFICIENCY TRACKER
#This program helps a driver find out what their vehicle actually costs to
#drive. Every time the driver stops for gas, they enter three numbers from
#the pump and the dashboard: the odometer reading, the gallons pumped, and
#the price per gallon. The program stores those entries, calculates the gas
#mileage for each tank, reports the driver's best, worst, and overall average
#mileage, works out the cost of every mile driven, and can estimate the fuel
#cost of a future road trip. The finished summary is saved to a text file so
#the driver can keep a running history over time.

#Bringing in the Fillup class, which stores one visit to the gas station.
from fillup import Fillup
#Bringing in the FuelLog class, which holds all the fill-ups together.
from fuellog import FuelLog
#Bringing in the datetime tool so each saved report can be stamped with the
#date and time it was created.
from datetime import datetime


#This function asks the user a question and refuses to move on until they
#type a number that is greater than zero. It exists because a user might type
#a word, a blank line, or a negative number by accident, and any of those
#would either crash the program or produce nonsense results. The loop keeps
#repeating until a good value is finally entered.
def askForNumber(question):
    while True:
        userInput = input(question)
        #Try to turn whatever the user typed into a decimal number.
        try:
            value = float(userInput)
        #If the text cannot be turned into a number, explain and ask again.
        except ValueError:
            print("That is not a number. Please enter a number such as 12.5.")
            continue
        #Reject zero and negative numbers, since neither makes sense here.
        if value <= 0:
            print("Please enter a number greater than zero.")
            continue
        #The value passed every check, so send it back to the caller.
        return value


#This function walks the user through entering one complete fill-up and adds
#it to the log. It also guards against an odometer reading that is smaller
#than the previous one, because a car's mileage can only ever go up. If that
#happened, the program would calculate a negative distance and report
#impossible gas mileage.
def addFillupToLog(log):
    print()
    print("--- Adding fill-up number", log.getCount() + 1, "---")
    odometer = askForNumber("Odometer reading in miles: ")

    #If earlier fill-ups exist, compare against the most recent odometer
    #reading and reject anything that has gone backwards.
    if log.getCount() > 0:
        lastFillup = log.fillups[log.getCount() - 1]
        while odometer <= lastFillup.getOdometer():
            print("The odometer cannot go backwards. Your last reading was",
                  lastFillup.getOdometer(), "miles.")
            odometer = askForNumber("Odometer reading in miles: ")

    gallons = askForNumber("Gallons of fuel pumped: ")
    price = askForNumber("Price per gallon in dollars: ")

    #Build the fill-up record and store it in the log.
    fillup = Fillup(odometer, gallons, price)
    log.addFillup(fillup)
    print("Saved:", fillup)

    #Remind the driver that one lone fill-up is not yet enough to do the math.
    if not log.hasEnoughData():
        print("Note: enter one more fill-up before mileage can be calculated.")


#This function prints the full summary of everything the program has worked
#out from the fill-ups entered so far.
def showReport(log):
    print()
    print("========================================")
    print("FUEL REPORT FOR", log.getVehicleName().upper())
    print("========================================")

    #Mileage always needs two fill-ups to compare, so stop early if there
    #are not enough entries and tell the user why.
    if not log.hasEnoughData():
        print("Not enough data yet. At least two fill-ups are needed,")
        print("because gas mileage is measured between two stops.")
        print("Fill-ups recorded so far:", log.getCount())
        return

    #Print the mileage figure for each individual tank of fuel.
    mpgList = log.getMpgList()
    tankNumber = 1
    for mpg in mpgList:
        print("Tank %d: %.2f miles per gallon" % (tankNumber, mpg))
        tankNumber += 1

    #Print the combined statistics for the whole log.
    print("----------------------------------------")
    print("Total miles driven: %.1f" % log.getTotalMiles())
    print("Total spent on fuel: $%.2f" % log.getTotalCost())
    print("Average mileage: %.2f miles per gallon" % log.getAverageMpg())
    print("Best tank: %.2f miles per gallon" % log.getBestMpg())
    print("Worst tank: %.2f miles per gallon" % log.getWorstMpg())
    print("Fuel cost per mile: $%.3f" % log.getCostPerMile())
    print("========================================")


#This function estimates the fuel cost of a road trip the driver is planning.
#It uses the driver's own cost per mile, so the answer reflects how this
#particular vehicle has really been performing rather than a generic guess.
def estimateTrip(log):
    print()
    #Without two fill-ups there is no cost per mile, so no estimate is possible.
    if not log.hasEnoughData():
        print("An estimate needs at least two fill-ups first.")
        return
    tripMiles = askForNumber("How many miles is your planned trip? ")
    cost = log.estimateTripCost(tripMiles)
    gallonsNeeded = tripMiles / log.getAverageMpg()
    print("A %.1f mile trip should use about %.2f gallons" %
          (tripMiles, gallonsNeeded))
    print("and cost roughly $%.2f in fuel." % cost)


#This function writes the finished report out to a text file named
#fuel_report.txt. The file is opened in append mode, which means each new
#report is added to the bottom of the file instead of erasing what came
#before, giving the driver a running history.
def saveReport(log):
    #Nothing meaningful can be saved without enough fill-ups.
    if not log.hasEnoughData():
        print("There is not enough data to save a report yet.")
        return

    #Try to open and write the file, and report a clear message if the
    #computer will not allow it, for example if the disk is protected.
    try:
        reportFile = open("fuel_report.txt", "a")
    except IOError:
        print("The report file could not be opened, so nothing was saved.")
        return

    #Get the current date and time and format it for the report heading.
    now = datetime.now()
    stamp = now.strftime("%m/%d/%Y %H:%M:%S")

    reportFile.write("\n\n=== Fuel report generated " + stamp + " ===")
    reportFile.write("\nVehicle: " + log.getVehicleName())
    reportFile.write("\nFill-ups recorded: " + str(log.getCount()))
    reportFile.write("\nTotal miles driven: %.1f" % log.getTotalMiles())
    reportFile.write("\nTotal spent on fuel: $%.2f" % log.getTotalCost())
    reportFile.write("\nAverage mileage: %.2f MPG" % log.getAverageMpg())
    reportFile.write("\nBest tank: %.2f MPG" % log.getBestMpg())
    reportFile.write("\nWorst tank: %.2f MPG" % log.getWorstMpg())
    reportFile.write("\nFuel cost per mile: $%.3f" % log.getCostPerMile())

    #Close the file so the writing is finished and saved properly.
    reportFile.close()
    print("The report was saved to fuel_report.txt")


#This function prints the list of choices the user can pick from.
def showMenu():
    print()
    print("What would you like to do?")
    print("  1 - Add a fill-up")
    print("  2 - See my fuel report")
    print("  3 - Estimate the cost of a trip")
    print("  4 - Save my report to a file")
    print("  5 - Quit")


#The main function is the starting point of the program. It greets the user,
#creates the log, then repeats the menu over and over until the user chooses
#to quit.
def main():
    print("========================================")
    print("       FUEL EFFICIENCY TRACKER")
    print("========================================")
    print("Track what your vehicle really costs to drive.")

    #Ask for the vehicle nickname and keep asking if the user just hits enter.
    vehicleName = input("What do you call your vehicle? ")
    while vehicleName.strip() == "":
        print("Please type a name, for example: My Truck")
        vehicleName = input("What do you call your vehicle? ")

    #Create the empty log that will hold all of this vehicle's fill-ups.
    log = FuelLog(vehicleName.strip())
    running = True

    #Keep showing the menu until the user picks the quit option.
    while running:
        showMenu()
        choice = input("Enter your choice (1-5): ")

        #Send the user to the matching function based on what they typed.
        if choice == "1":
            addFillupToLog(log)
        elif choice == "2":
            showReport(log)
        elif choice == "3":
            estimateTrip(log)
        elif choice == "4":
            saveReport(log)
        elif choice == "5":
            #Turning this switch off ends the loop and the program.
            running = False
            print()
            print("Thanks for tracking with us. Drive safe!")
        else:
            #Anything other than 1 through 5 is not a valid menu choice.
            print("That is not a valid choice. Please enter 1, 2, 3, 4, or 5.")


#This line makes sure the main function only runs when this file is the one
#being started, which is the standard way to launch a Python program.
if __name__ == "__main__":
    main()
