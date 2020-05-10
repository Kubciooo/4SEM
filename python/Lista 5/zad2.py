import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
data=pd.read_csv('ratings1.csv')
movie_names = pd.read_csv('movies1.csv')
ratings_data= data[data.movieId < 10000].to_numpy()
x = np.zeros((611,10000))

y = [0 for i in range(10000)]
y[1] = 5   # patrz movies.csv  2571 - Matrix
y[3] =2
y[32] = 5    #y[32] = 4
y[1097] = 5        # 32 - Twelve Monkeys
y[260] = 5       # 260 - Star Wars IV
y[1097] = 4
y = np.array([y])
for row in ratings_data[1:]:
    x[int(row[0])][int(row[1])] = float(row[2])


Z = cosine_similarity(x,[y.flatten()])
#dla podejścia ze strony Z = np.dot(np.nan_to_num(x/np.linalg.norm(x, axis=0)), y/np.linalg.norm(y))
R = cosine_similarity(x.T, [Z.flatten()])
#dla podejścia ze strony X = np.nan_to_num(x/np.linalg.norm(x, axis=0))
#dla podejścia ze strony R = np.dot(X.T, z/np.linalg.norm(z))
x = np.sort(R, axis=0)[::-1]
for i in range(5):
    id = np.where(R == x[i])[0][0]
    movie_name = movie_names[movie_names.movieId == id].title.to_string()
    movie_name = ' '.join(movie_name.split(' ')[4:])
    print((x[i][0], id, movie_name))
