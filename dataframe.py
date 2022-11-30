import pandas as pd 



colums = ['TNR', 'num_kittens', 'health', 'borough', 'neighborhood', 'relative_loc', 'food', 'color','latitude', 'longitude' ]
 
col = {i:[''] for i in colums}

df = pd.DataFrame(col)
print(df)


df.to_csv('TNR_data.csv')