#!python3.9

from datetime import date
import os
import connection

import pandas as pd
import numpy as np

if __name__ == "__main__":
    path = os.getcwd()
    path_query = path + '/sql/'

    #file_query
    file_query = 'dump_query.sql'

    #connection
    conn = connection.db_connect()
    cur = conn.cursor()

    #read_data
    with open(path_query + file_query,'r') as file:
        query = file.read()

    cur.execute(query)
    data = cur.fetchall() 
    df = pd.DataFrame(data, columns=['order','costumer','city','date'])

    #transformation
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['date'].dt.year == 2016]
    df['date'] = df['date'].dt.strftime('%Y-%m-%d')

    df \
        .groupby(['city','date']) \
        .agg({'order':'count'}) \
        .unstack() \
        .to_excel('report_order.xlsx')   

    df \
        .groupby(['city','date']) \
        .agg({'costumer':'nunique'}) \
        .unstack() \
        .to_excel('report_costumer.xlsx')  