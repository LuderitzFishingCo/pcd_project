# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 09:16:09 2021

@author: ndesh
"""

import pandas as pd

df = pd.read_excel('PCD_DB.xlsx')
film_df = df.loc[df["Type"] == "Film"]
series_df = df.loc[df['#'] >= 1]

film_df.drop('#', inplace =True, axis =1 )
film_df.drop('Type', inplace =True, axis =1 )

series_df.drop('Type', inplace =True, axis =1 )
series_df.drop('Medium', inplace =True, axis =1 )

film_df.to_csv('films_pcd.csv',index = False)
series_df.to_csv('series_pcd.csv',index = False)
