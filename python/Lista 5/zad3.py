import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
data=pd.read_csv('ratings.csv')
movie_names = pd.read_csv('movies.csv')


y = np.zeros((data.movieId.max()+1,1))
y[1] = 5   # patrz movies.csv  2571 - Matrix
y[3] =2
y[32] = 5    #y[32] = 4
y[1097] = 5        # 32 - Twelve Monkeys
y[260] = 5       # 260 - Star Wars IV
y[1097] = 4
y = np.array([y])
x = sparse.coo_matrix((data.rating[1:], (data.userId[1:], data.movieId[1:])))


Z = cosine_similarity(x,[y.flatten()])
R = cosine_similarity(x.T, [Z.flatten()])

x = np.sort(R, axis=0)[::-1]
for i in range(5):
    id = np.where(R == x[i])[0][0]
    movie_name = movie_names[movie_names.movieId == id].title.to_string()
    movie_name = ' '.join(movie_name.split(' ')[4:])
    print((x[i][0], id, movie_name))

