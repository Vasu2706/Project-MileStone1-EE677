import os
import pandas as pd
from metrics import clean_states
from ac import add_ac

states = clean_states(pd.read_excel("data/state.xlsx"))
ac_capacity = pd.read_csv("data/ac_capacity.csv", index_col='Year')
ac_demand = pd.read_csv("data/ac_demand.csv", index_col='Year')
ac_stock_base = pd.read_csv("data/ac_stock_base.csv", index_col='Year')
ac_stock = pd.read_csv("data/ac_stock.csv", index_col='Year')

def run_ac():
    for efficiency in ['baseline', 'iea']:
        for year in [2020, 2025, 2030, 2035, 2040, 2045, 2050]:
            res_ac, com_ac = add_ac(efficiency, year, states, ac_stock, ac_stock_base, ac_demand, ac_capacity)
            res_ac.to_csv('res_'+efficiency+'_'+str(year)+'.csv')
            com_ac.to_csv('com_'+efficiency+'_'+str(year)+'.csv')
    dirlist = os.listdir('input/ac/')
    for file in dirlist:
        df = pd.read_csv('input/ac/'+file, index_col=0)
        df = df*1000
        df.to_csv('input/ac/'+file)
