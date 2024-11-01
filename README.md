# Project-MileStone1-EE677

## Project Overview


- **forecast.py**: Contains functions to build the hourly demand of various technologies.
- **results.py**: Generates all the hourly profiles at different resolutions.

The project also organizes scenarios using a hierarchical folder structure. Each path to a CSV file corresponds to a specific scenario, with the breakdown as follows:

1. **GDP Growth**: Options are `slow`, `stable`, `rapid`.
2. **Cooling**: Options are `baseline`, `efficient`.
3. **Type**: Options are `detailed` (hourly demand profiles with 8760 rows) and `summary` (annual consumption summaries with 7 rows).

### File Descriptions

- **Detailed**: Contains itemized hourly demand profiles for each scenario, producing 8760 rows (one for each hour in a year).
- **Summary**: Contains itemized annual energy consumption data for each scenario, with 7 rows representing considered future years.

Each file path serves as a reference to the scenario represented within the data tables. For example, `SR.csv` in the path `slow/efficient/summary` provides a summary for a scenario of slow economic growth and energy-efficient air conditioning demand.

### Data Table Structure (Table 3)

| Column Header | Description |
|---------------|-------------|
| DateTime      | Hourly or yearly time resolution |
| Base          | Business-as-usual model resulting demand |
| Com AC        | Commercial Air Conditioning demand |
| Res AC        | Residential Air Conditioning demand |


