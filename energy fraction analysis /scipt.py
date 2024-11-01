import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = 'scipt.py/India_efficiency.csv'
data = pd.read_csv(file_path)

# Rename the 'Unnamed: 0' column to 'Year'
data.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)

# Convert the units from MWh to TWh for 'Com AC' and 'Res AC' columns
data['Com AC (TWh)'] = data['Com AC'] / 1e6
data['Res AC (TWh)'] = data['Res AC'] / 1e6

# Filter out the year 2020
data_filtered = data[data['Year'] != 2020]

# Set up the plot
plt.figure(figsize=(10, 6))

# Plot 'Com AC' and 'Res AC' columns as a stacked bar chart
plt.bar(data_filtered['Year'].astype(str), data_filtered['Com AC (TWh)'], label='Commercial AC (TWh)')
plt.bar(data_filtered['Year'].astype(str), data_filtered['Res AC (TWh)'], 
        bottom=data_filtered['Com AC (TWh)'], label='Residential AC (TWh)')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Energy Consumption (TWh)')
plt.title('Projected Energy Consumption for AC in India (2025 Onwards) Energy Efficient Scenerio')
plt.legend()

# Show the plot
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
