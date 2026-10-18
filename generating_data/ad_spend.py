import matplotlib.pyplot as plt 

#1 prepare the data
ad_spend_usd = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
# new-customers = [5, 12, 19, 23, 22,38, 44, 41, 56, 62]
new_customers = [5, 12, 19, 23, 22,38, 44, 41, 56, 62]

#2 plot data
plt.figure(figsize=(7,5))
plt.scatter(ad_spend_usd, new_customers)


#3 Customize layout 
plt.title('Marketing Impact: Add Spend vs Conversions',  fontsize=14, fontweight='bold')
plt.xlabel('Ad Budget ($)')
plt.ylabel('New Sign Up')
plt.grid(True, alpha=0.6)

plt.show()



