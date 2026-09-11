# Fuel Efficiency Tracker

**Track your vehicle's true cost of ownership with a simple, powerful command-line tool.**

Fuel Efficiency Tracker is a Python-based utility designed to help drivers understand exactly how much their vehicles cost to operate. By logging fill-up data at the pump, this tool calculates comprehensive fuel economy metrics and provides actionable insights into your driving costs.

## Features

- **Track Fill-Ups**: Record odometer readings, gallons pumped, and price per gallon each time you fuel up
- - **Calculate MPG**: Get accurate miles-per-gallon calculations for each tank and overall averages
  - - **Cost Analysis**: Discover your true fuel cost per mile and see how individual tanks compare
    - - **Trip Estimation**: Estimate the fuel cost and gallons needed for planned road trips based on your actual vehicle performance
      - - **Performance History**: Identify your best and worst fuel efficiency tanks to spot patterns
        - - **Persistent Reports**: Save detailed reports to a file, building a running history of your vehicle's performance over time
         
          - ## How It Works
         
          - The program follows a straightforward workflow:
         
          - 1. **Name Your Vehicle**: Start by giving your vehicle a nickname for identification
            2. 2. **Log Fill-Ups**: Each time you fill up, enter:
               3.    - Odometer reading (miles)
                     -    - Gallons of fuel pumped
                          -    - Price per gallon (in dollars)
                               - 3. **View Reports**: See instant calculations for MPG, costs, and efficiency stats
                                 4. 4. **Plan Trips**: Get fuel cost estimates for upcoming road trips
                                    5. 5. **Save History**: Export reports to a text file for long-term tracking
                                      
                                       6. ## Getting Started
                                      
                                       7. ### Prerequisites
                                       8. - Python 3.x
                                         
                                          - ### Installation
                                          - Simply clone this repository and run the program:
                                         
                                          - ```bash
                                            python main.py
                                            ```

                                            ### Usage
                                            The program presents a menu-driven interface:

                                            ```
                                            What would you like to do?
                                             1 - Add a fill-up
                                             2 - See my fuel report
                                             3 - Estimate the cost of a trip
                                             4 - Save my report to a file
                                             5 - Quit
                                            ```

                                            **Note**: You'll need to enter at least two fill-ups before fuel economy calculations become available (since MPG is measured between two data points).

                                            ## Example Workflow

                                            ```
                                            What do you call your vehicle? My Truck

                                            --- Adding fill-up number 1 ---
                                            Odometer reading in miles: 12500
                                            Gallons of fuel pumped: 15.5
                                            Price per gallon in dollars: 3.45

                                            [Add another fill-up to enable calculations...]

                                            --- Adding fill-up number 2 ---
                                            Odometer reading in miles: 12750
                                            Gallons of fuel pumped: 16.2
                                            Price per gallon in dollars: 3.52

                                            Tank 1: 16.13 miles per gallon
                                            ----------------------------------------
                                            Total miles driven: 250.0
                                            Total spent on fuel: $55.24
                                            Average mileage: 16.13 miles per gallon
                                            Fuel cost per mile: $0.221
                                            ```

                                            ## Output Files

                                            - **fuel_report.txt**: A cumulative report file that saves timestamped summaries each time you export. This gives you a historical record of your vehicle's performance over time.
                                           
                                            - ## Project Structure
                                           
                                            - - `main.py`: The primary entry point; contains the menu system and user interaction logic
                                              - - `fillup.py`: Defines the Fillup class for storing individual fill-up data
                                                - - `fuellog.py`: Defines the FuelLog class for managing collections of fill-ups and performing calculations
                                                 
                                                  - ## Data Validation
                                                 
                                                  - The program includes safeguards to prevent common user errors:
                                                  - - Rejects non-numeric input
                                                    - - Prevents zero or negative values
                                                      - - Guards against odometer readings going backwards (physically impossible)
                                                        - - Requires at least two fill-ups before calculations
                                                         
                                                          - ## Why Track Your Fuel Efficiency?
                                                         
                                                          - Understanding your vehicle's true cost helps you:
                                                          - - **Identify trends**: Spot when your MPG drops (indicating maintenance issues)
                                                            - - **Optimize routes**: Use actual cost data to plan fuel-efficient trips
                                                              - - **Budget accurately**: Know exactly how much fuel expenses eat into your budget
                                                                - - **Monitor vehicle health**: Sudden drops in efficiency often signal mechanical problems
                                                                 
                                                                  - ## License
                                                                 
                                                                  - This project is open source. Feel free to use, modify, and distribute it.
                                                                 
                                                                  - ## Contributing
                                                                 
                                                                  - Contributions are welcome! Whether it's bug fixes, feature suggestions, or improvements to the user experience, please feel free to submit issues or pull requests.
                                                                 
                                                                  - ---

                                                                  **Start tracking today and take control of your vehicle's fuel costs!**
