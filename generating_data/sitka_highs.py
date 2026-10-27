from pathlib import Path
import csv 
import matplotlib.pyplot as plt # Plot the data in a temperature chart
from datetime import datetime


# we read the file and change the splitlines() method to get a list of all lines in the file 
path = Path(__file__).parent / 'weather_data/sitka_weather_2021_simple.csv'
lines = path.read_text().splitlines()

# Extract high temperatures before plotting them.
reader = csv.reader(lines) # we use a reader object that can be used to parse each line in the file.To make a reader  object, call the function csv.reader() and pass it in the list of lines from the CSV file 
header_row = next(reader) # when given the reader object(), the next() function returns the next line in the file starting from the beginning of the file 




# highs = [int(row[4]) for row in reader]
# Extract dates and high temperatures.
dates, highs, lows = [], [],[] # convert the data containing the date information (row[2]) to a datetime object temperature values to plot()

for row in reader:
  current_date = datetime.strptime(row[2], '%Y-%m-%d')
  high = int(row[4])
  low = int(row[5])
  dates.append(current_date)
  highs.append(high)
  lows.append(low)


# Plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color = 'red', alpha = 0.5) # An alpha value of 0 is transparent, and a value of 1 is completely opaque. By setting alpha to 0.5 we make the red and blue plot lines appear lighter 
ax.plot(dates, lows, color = 'blue', alpha = 0.5)
ax.fill_between(dates, highs, lows, facecolor = 'blue', alpha = 0.1) # The facecolor argument determines the color of the shaded region; we give it a low alpha value of 0.1  so the field region connects the two data series without distracting from the information they represent 

# Format plot.
ax.set_title("Daily High and Low Temperatures, 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate() # draws the date labels diagonally to prevent them from overlapping
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()



# for index,column_header in enumerate(header_row):
#   print(index, column_header)

# print (highs)


# print(header_row)