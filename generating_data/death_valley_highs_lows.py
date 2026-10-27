# error checking
from pathlib import Path
import csv
import matplotlib.pyplot as plt 
from datetime import datetime

path = Path(__file__).parent / 'weather_data/death_valley_2021_simple.csv'
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# for index, column_header in enumerate(header_row):
#   print(index, column_header)

# Extract dates, and high and low temperatures.
dates, highs, lows = [], [], []
for row in reader:
  current_date = datetime.strptime(row[2], '%Y-%m-%d')
  try:
    high = int(row[3])
    low = int(row[4])
  except ValueError:
    print(f"Missing data for {current_date}")
  else:
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
title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)




