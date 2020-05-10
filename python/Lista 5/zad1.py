import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def a(m):
    data=pd.read_csv('ratings1.csv')
    P = data[data.movieId == 1].userId.to_numpy()

    M = data[data.userId.isin(P)]
    M = M[M.movieId <= m+1].to_numpy()
    x = np.zeros((215, m+1))
    y = np.zeros((215,1))
    previous = 0 
    i = -1 
    for user,movie,rating,timestamp in M:
        if user != previous: 
                i += 1
        if int(movie) == 1: 
            y[i][int(movie)-1] = rating
        else:
            x[i][int(movie)-2] = rating 
        previous = user

    clf = LinearRegression().fit(x,y)
    return clf.predict(x) - y



def b(m):
    print("M = ",m)
    data=pd.read_csv('ratings1.csv')
    P = data[data.movieId == 1].userId.to_numpy()
    M = data[data.userId.isin(P)]
    M = M[M.movieId <= m+1].to_numpy()
    x = np.zeros((200, m+1))
    x_testers = np.zeros((15,m+1))
    y = np.zeros((200,1))
    y_testers = np.zeros((15,1))
    previous = 0 
    i = -1 
    for user,movie,rating,timestamp in M:
        if user != previous: 
                i += 1
        if i < 200:
            if int(movie) == 1: 
                y[i][int(movie)-1] = rating
            else:
                x[i][int(movie)-2] = rating 
            previous = user
        else: 
            if int(movie) == 1: 
                y_testers[i-200][int(movie)-1] = rating
            else:
                x_testers[i-200][int(movie)-2] = rating 
            previous = user
    clf = LinearRegression().fit(x,y)
    for i in range(len(x_testers)):
        print(i, " predict: ", clf.predict([x_testers[i]])[0][0], ', y:',y_testers[i][0])
    print("\n")

fig, ax = plt.subplots(3)

ax[0].plot([i for i in range(215)], a(10), label="m=10")
ax[0].set_title("różnica wartości przewidywanej i prawidłowej dla m=10")
ax[1].plot([i for i in range(215)], a(1000),label=" m=1000")
ax[1].set_title("m=1000")
ax[2].plot([i for i in range(215)], a(10000),label="m=10000")
ax[0].set_title("Różnica wartości przewidywanej i prawidłowej")
ax[0].legend(loc="lower right")
ax[1].legend(loc="lower right")
ax[2].legend(loc="lower right")

b(10)
b(100)
b(200)
b(500)
b(1000)
b(10000)

plt.show()
