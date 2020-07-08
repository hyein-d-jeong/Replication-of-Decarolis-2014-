import pandas as pd
import numpy as np
import matplotlib as plt
from linearmodels import PanelOLS
import statsmodels.api as sm
import econtools as econ
import econtools.metrics as mt
from statsmodels.stats.outliers_influence import variance_inflation_factor

from auxiliary.prepare import *
from auxiliary.table2 import*
from auxiliary.table_formula import *

#df_table = pd.DataFrame({ 'Panel':[], 'value_title':[],'Control(1)':[],'Control(2)':[],'Control(3)':[],'Control(4)':[],'Control(5)':[],'Control(6)':[]})
#value_title = ['First Auction Price','Standard Error','R$^2$','Observations']
#Panel =['A','B','C','D']

def reg_tab(parameter, data, column):
    table_string = econ.outreg(parameter, ['fpsb_auction'], ['First Price Auction'], digits = 2)
    table_string += econ.table_statrow("R$^2$", [x.r2 for x in parameter], digits =3)
    table_string += econ.table_statrow("Number of Observation", [x.N for x in parameter])
    table_list = table_string.split('&')
    table_list = [i.split('\\\\ \n',1)[0] for i in table_list]
    table_list.remove(table_list[0])
    
    df_table = data

    for i in range(len(table_list)):
        df_table.loc[i, 'Control'+'('+str(column)+')'] = table_list[i]
        if i<4:
            df_table.loc[i,'value_title'] = value_title[0]
        elif i>=4 and i<8:
            df_table.loc[i,'value_title'] = value_title[1]
        elif i>=8 and i<12:
            df_table.loc[i,'value_title'] = value_title[2]
        else:
            df_table.loc[i,'value_title'] = value_title[3]

    for i in range(0,4):
        if i ==0:
            df_table.loc[i,'Panel'] =Panel[i]
            df_table.loc[i+4,'Panel'] =Panel[i]
            df_table.loc[i+8,'Panel'] =Panel[i]
            df_table.loc[i+12,'Panel'] =Panel[i]
        elif i == 1:
            df_table.loc[i,'Panel'] =Panel[i+1]
            df_table.loc[i+4,'Panel'] =Panel[i+1]
            df_table.loc[i+8,'Panel'] =Panel[i+1]
            df_table.loc[i+12,'Panel'] =Panel[i+1]
        elif i == 2:
            df_table.loc[i,'Panel'] =Panel[i-1]
            df_table.loc[i+4,'Panel'] =Panel[i-1]
            df_table.loc[i+8,'Panel'] =Panel[i-1]
            df_table.loc[i+12,'Panel'] =Panel[i-1]
        elif i == 3:
            df_table.loc[i,'Panel'] =Panel[i]
            df_table.loc[i+4,'Panel'] =Panel[i]
            df_table.loc[i+8,'Panel'] =Panel[i]
            df_table.loc[i+12,'Panel'] =Panel[i]

    df_table = df_table.sort_values(by='Panel',ascending = True).set_index(['Panel','value_title'])

    return(df_table)