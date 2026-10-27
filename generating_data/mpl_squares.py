import matplotlib.pyplot as plt #so we 

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots() 
#subplots function can generate one or more plots on the same graph
#the variable fig represents the entire figure which is a collection of plots generated 
#The variable ax represents a single plot in the figure ; this is the variable we'll  use most of the time when defining and customizing a single plot 
ax.plot(input_values,squares, linewidth=3)

# Set chart title and label axes.
ax.set_title("Square Numbers", fontsize=24) # the set_title() method sets an overall title for the chart. Font size parameters ,which appear repeatedly throughout the code 
ax.set_xlabel("Value", fontsize=24) # Set_xlabel methods allow to set a title for each axes 
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(labelsize=14) # sets the font size of the thick mark labels to 14 on both axes 

plt.show()
# The function plt.show opens matplotlib and displays the plot 