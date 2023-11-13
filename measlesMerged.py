# Load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import andrews_curves


# Load measles cases data
measles_data = pd.read_csv('fallzahlennachbundesland.csv', sep=',')

# Load vaccination rates data
vaccination_data = pd.read_csv('geimpftekindernachbundesländern2015.csv', sep=',')

# Merge data
merged_data = pd.merge(measles_data, vaccination_data, on='Bundesland')

# Explore data
print(merged_data.head())

# Bar chart for measles cases
# Line plot for both measles cases and vaccination rates
plt.figure(figsize=(12,6))

# Plot measles cases
plt.plot(merged_data['Bundesland'], merged_data['Masernzahlen'], label='Measles Cases', color='pink')

# Plot vaccination rates
plt.plot(merged_data['Bundesland'], merged_data['Impfrate'], label='Vaccination Rate', color='purple')

plt.xlabel('Bundesland')
plt.ylabel('Values')
plt.title('Measles Cases and Vaccination Rates per Bundesland')
plt.legend()
plt.show()
