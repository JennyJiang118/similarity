from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import sys
from matplotlib import pyplot
import time
import math

#%%
sys.path.insert(0,".")
path = "data/full_music_data.csv"
data = pd.read_csv(path, converters={u'year':int})

path_genre = "data/genre.xlsx"
data_genre = pd.read_excel(path_genre, converters={u'id':int})







#%%
#----------------data process-------------#
data = data.drop(['artist_names','song_title (censored)','release_date'],1)
data['genre'] = ''
data['artists_id'] = data.artists_id.apply(lambda x:x[1:-1])

#%%
# 寻找曲风
genres = ['Avant-Garde','Blues',"Children's",'Classical','Comedy/Spoken','Country','Easy Listening','Electronic',
          'Folk','International','Jazz','Latin','New Age','Pop/Rock','R&B;','Reggae','Religious','Stage & Screen',
          'Unknown','Vocal']

for i in range(len(data)):
    if ',' in data.loc[i,'artists_id']:
        idx = data.loc[i,'artists_id'].find(',')
        data.loc[i, 'artists_id'] = data.loc[i,'artists_id'][0:idx]


    for j in range(len(data_genre)):
        if int(data.loc[i,'artists_id']) == data_genre.loc[j,'id']:
            data.loc[i,'genre'] = data_genre.loc[j,'genre']
            break
        elif int(data.loc[i,'artists_id']) < data_genre.loc[j,'id']:
            data.loc[i,'genre'] = 'Unknown'
            break





#%%
#-----------------standard----------------#
data_d = data[:,1:-1]
for i in range(data_d.shape[1]):
    mean = np.mean(data_d.iloc[:,i])
    std = np.var(data_d.iloc[:,i])
    data_d.iloc[:,i] = (data_d.iloc[:,i]-mean)/std

data['similarity'] = ''



#%%
# 验证similariy:取前10
idx1 = 0
idx2 = 1
x1 = data[idx1, 1:-1]
x2 = data[idx2, 1:-1]
similarity = math.sqrt()

