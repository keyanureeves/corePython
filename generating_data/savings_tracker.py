import matplotlib.pyplot as plt 

#1 prepare the data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
savings = [450, 520, 490, 610, 700, 750]

#2 Plot Data and customize 
plt.figure(figsize=(8,4))
plt.plot(months, savings, marker='o', color='#2ca02c', linestyle='--', linewidth=2)

#3 Add labels and context
plt.title('Monthly Savings Trend', fontsize=14, fontweight='bold')
plt.xlabel('Months')
plt.ylabel('Amount Saved')
plt.grid(True, linestyle=':', alpha=0.6)

plt.show()

