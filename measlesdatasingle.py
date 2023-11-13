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

plt.figure(figsize=(12, 6))
plt.plot(merged_data['Bundesland'], merged_data['Masernzahlen'], label='Measles Cases', color="pink")
plt.xlabel('Bundesland')
plt.ylabel('Measles Cases')
plt.title('Measles Cases per Bundesland in 2015')
plt.legend()
plt.show()

# Bar chart for vaccination rates
plt.figure(figsize=(12, 6))
plt.plot(merged_data['Bundesland'], merged_data['Impfrate'], label='Vaccination Rate', color="purple")
plt.xlabel('Bundesland')
plt.ylabel('Vaccination Rate')
plt.title('Vaccination Rates per Bundesland in 2019')
plt.legend()
plt.show()
