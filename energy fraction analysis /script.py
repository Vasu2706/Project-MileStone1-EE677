import matplotlib.pyplot as plt
import pandas as pd

# Load the data from the provided CSV files
baseline_data = pd.read_csv('India_baseline.csv')
energy_efficient_data = pd.read_csv('India Energy Efficient.csv')

# Display the first few rows of each data to understand its structure and identify relevant columns
print("Baseline Data:")
print(baseline_data.head())
print("\nEnergy Efficient Data:")
print(energy_efficient_data.head())

# Define years column
years = energy_efficient_data['Unnamed: 0']

# Calculate total space cooling for each year (Com AC + Res AC) for both scenarios
energy_efficient_data['Total Space Cooling'] = energy_efficient_data['Com AC'] + energy_efficient_data['Res AC']
baseline_data['Total Space Cooling'] = baseline_data['Com AC'] + baseline_data['Res AC']

# Calculate the fraction of space cooling relative to total base energy consumption for each year
energy_efficient_data['Fraction Space Cooling'] = energy_efficient_data['Total Space Cooling'] / (energy_efficient_data['Total Space Cooling'] + energy_efficient_data['Base'])
baseline_data['Fraction Space Cooling'] = baseline_data['Total Space Cooling'] / (baseline_data['Total Space Cooling'] + baseline_data['Base'])

# Extract the fraction for the year 2050 for both cases
fraction_2050_energy_efficient = energy_efficient_data.loc[energy_efficient_data['Unnamed: 0'] == 2050, 'Fraction Space Cooling'].values[0]
fraction_2050_baseline = baseline_data.loc[baseline_data['Unnamed: 0'] == 2050, 'Fraction Space Cooling'].values[0]

# Plot the fraction of space cooling for each year in both scenarios
plt.figure(figsize=(12, 6))
bars1 = plt.bar(years - 0.2, energy_efficient_data['Fraction Space Cooling'], width=0.4, label='Energy Efficient Scenario')
bars2 = plt.bar(years + 0.2, baseline_data['Fraction Space Cooling'], width=0.4, label='Baseline Scenario')

# Labels and title
plt.xlabel('Year')
plt.ylabel('Fraction of Space Cooling (Relative to Total Base Energy Consumption)')
plt.title('Fraction of Space Cooling for Each Year in Energy Efficient and Baseline Scenarios')
plt.legend()
plt.xticks(years, rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adding fraction values above the bars
for bar in bars1:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}", ha='center', va='bottom')

for bar in bars2:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f"{yval:.2f}", ha='center', va='bottom')

# Display the plot
plt.tight_layout()
plt.show()

# Show the fraction values for the year 2050 in both scenarios
print("\nFraction of Space Cooling in 2050:")
print("Energy Efficient Scenario:", fraction_2050_energy_efficient)
print("Baseline Scenario:", fraction_2050_baseline)
