""" Created by Cyouisme """
# 08/20/2022
# -*-encoding:utf-8-*-

import pandas as pd

file = pd.read_csv("data_final_pro_2_crawl_nha_hang_500.csv")

f = file.copy()

for i in f.iloc[0:109, 2:8]:
	f[i][0:109] = f[i][0:109].fillna(0)

# print(f.head())


#Define csv to utf8 for vietnamese
f.to_csv("./danang/data_final_pro_2_crawl_nha_hang_500.csv", encoding='utf-8-sig')