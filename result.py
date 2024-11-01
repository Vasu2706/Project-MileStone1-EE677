import pandas as pd
import os
from metrics import clean_states

def results():
    states = clean_states(pd.read_excel("data/state.xlsx"))

    # Create necessary directories if they don't exist
    for growth in ['stable', 'rapid', 'slow']:
        for efficiency in ['baseline', 'iea']:
            if not os.path.exists(f'results/{growth}/{efficiency}/region'):
                os.makedirs(f'results/{growth}/{efficiency}/region')
            if not os.path.exists(f'results/{growth}/{efficiency}/state'):
                os.makedirs(f'results/{growth}/{efficiency}/state')
            if not os.path.exists(f'results/{growth}/{efficiency}/national'):
                os.makedirs(f'results/{growth}/{efficiency}/national')

    for growth in ['stable', 'rapid', 'slow']:
        for efficiency in ['baseline', 'iea']:
            for year in [2020, 2025, 2030, 2035, 2040, 2045, 2050]:
                # Load data
                bau_profile = pd.read_csv(f'input/bau/bau_{growth}_{year}.csv')
                res_ac = pd.read_csv(f'input/ac/res_{efficiency}_{year}.csv')
                com_ac = pd.read_csv(f'input/ac/com_{efficiency}_{year}.csv')

                print(growth, efficiency, year)

                # Process data for each state
                for state in states.index.tolist()[:-1]:
                    state_df = pd.DataFrame()
                    state_df['Base'] = bau_profile[state]
                    state_df['Com AC'] = com_ac[state]
                    state_df['Res AC'] = res_ac[state]
                    state_df.index = bau_profile.DateTime
                    state_df.to_csv(f'results/{growth}/{efficiency}/state/{state}_{year}.csv')

                # Process data for each region
                for region in states.Region.unique().tolist()[:-1]:
                    regional_states = states[states.Region == region].index.tolist()
                    region_df = pd.DataFrame()
                    region_df['Base'] = bau_profile[regional_states].sum(axis=1)
                    region_df['Com AC'] = com_ac[regional_states].sum(axis=1)
                    region_df['Res AC'] = res_ac[regional_states].sum(axis=1)
                    region_df.index = bau_profile.DateTime
                    region_df.to_csv(f'results/{growth}/{efficiency}/region/{region}_{year}.csv')

                # Process data for the entire nation
                all_states = states.index.tolist()[:-1]
                national_df = pd.DataFrame()
                national_df['Base'] = bau_profile[all_states].sum(axis=1)
                national_df['Com AC'] = com_ac[all_states].sum(axis=1)
                national_df['Res AC'] = res_ac[all_states].sum(axis=1)
                national_df.index = bau_profile.DateTime
                national_df.to_csv(f'results/{growth}/{efficiency}/national/India_{year}.csv')

def result_summary():
    states = clean_states(pd.read_excel("data/state.xlsx"))

    # Create necessary summary directories if they don't exist
    for growth in ['stable', 'slow', 'rapid']:
        for efficiency in ['baseline', 'iea']:
            if not os.path.exists(f'results/{growth}/{efficiency}/summary'):
                os.makedirs(f'results/{growth}/{efficiency}/summary')

    for growth in ['stable', 'slow', 'rapid']:
        for efficiency in ['baseline', 'iea']:
            base, com_ac, res_ac = [], [], []
            for year in [2020, 2025, 2030, 2035, 2040, 2045, 2050]:
                df = pd.read_csv(f'results/{growth}/{efficiency}/national/India_{year}.csv')
                base.append(df.Base.sum())
                com_ac.append(df['Com AC'].sum())
                res_ac.append(df['Res AC'].sum())
            df = pd.DataFrame(zip(base, com_ac, res_ac), index=[2020, 2025, 2030, 2035, 2040, 2045, 2050], columns=['Base', 'Com AC', 'Res AC'])
            df.to_csv(f'results/{growth}/{efficiency}/summary/India.csv')

            for region in ['NR', 'ER', 'SR', 'WR', 'NER']:
                base, com_ac, res_ac = [], [], []
                for year in [2020, 2025, 2030, 2035, 2040, 2045, 2050]:
                    df = pd.read_csv(f'results/{growth}/{efficiency}/region/{region}_{year}.csv')
                    base.append(df.Base.sum())
                    com_ac.append(df['Com AC'].sum())
                    res_ac.append(df['Res AC'].sum())
                df = pd.DataFrame(zip(base, com_ac, res_ac), index=[2020, 2025, 2030, 2035, 2040, 2045, 2050], columns=['Base', 'Com AC', 'Res AC'])
                df.to_csv(f'results/{growth}/{efficiency}/summary/{region}.csv')

            for state in states.index.tolist()[:-1]:
                base, com_ac, res_ac = [], [], []
                for year in [2020, 2025, 2030, 2035, 2040, 2045, 2050]:
                    df = pd.read_csv(f'results/{growth}/{efficiency}/state/{state}_{year}.csv')
                    base.append(df.Base.sum())
                    com_ac.append(df['Com AC'].sum())
                    res_ac.append(df['Res AC'].sum())
                df = pd.DataFrame(zip(base, com_ac, res_ac), index=[2020, 2025, 2030, 2035, 2040, 2045, 2050], columns=['Base', 'Com AC', 'Res AC'])
                df.to_csv(f'results/{growth}/{efficiency}/summary/{state}.csv')


results()
result_summary()