# Load necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Ensure plots are displayed inline
%matplotlib inline

# Load measles cases data
measles_data = pd.read_csv('/PycharmProjects/examFOHI2023/fallzahlennachbundesland.csv', sep=',')

# Load vaccination rates data
vaccination_data = pd.read_csv('/PycharmProjects/examFOHI2023/geimpftekindernachbundesländern2015.csv', sep=',')

# Merge data
merged_data = pd.merge(measles_data, vaccination_data, on='Bundesland')

# Explore data
print(merged_data.head())

# Bar chart for measles cases
plt.figure(figsize=(12, 6))
plt.bar(merged_data['Bundesland'], merged_data['Masernzahlen'], label='Measles Cases')
plt.xlabel('Bundesland')
plt.ylabel('Measles Cases')
plt.title('Measles Cases per Bundesland in 2015')
plt.legend()
plt.show()

# Bar chart for vaccination rates
plt.figure(figsize=(12, 6))
plt.bar(merged_data['bundesland'], merged_data['vaccination_rate'], label='Vaccination Rate')
plt.xlabel('Bundesland')
plt.ylabel('Vaccination Rate')
plt.title('Vaccination Rates per Bundesland in 2019')
plt.legend()
plt.show()
