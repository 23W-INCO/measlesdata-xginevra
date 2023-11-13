import pandas as pd
import matplotlib.pyplot as plt

# Load measles cases data
measles_data = pd.read_csv('fallzahlennachbundesland.csv')

# Load vaccination rates data
vaccination_data = pd.read_csv('geimpftekindernachbundesländern2015.csv')

# Merge data
merged_data = pd.merge(measles_data, vaccination_data, on='Bundesland')

# Explore data
print(merged_data)

# Bar chart for measles cases
plt.figure(figsize=(12, 6))
plt.bar(merged_data['Bundesland'], merged_data['Masernzahlen'], label='Measles Cases')
plt.xlabel('Bundesland')
plt.ylabel('Measles Cases')
plt.title('Measles Cases per Bundesland in 2015')
plt.legend()

# Show the first plot
plt.show()

# Bar chart for vaccination rates
plt.figure(figsize=(12, 6))
plt.bar(merged_data['Bundesland'], merged_data['Impfrate'], label='Vaccination Rate')
plt.xlabel('Bundesland')
plt.ylabel('Vaccination Rate')
plt.title('Vaccination Rates per Bundesland in 2019')
plt.legend()

# Show the second plot
plt.show()
