'''
____________
|_S_|_X_|___|
|___|___|_E_|
|___|_X_|___|

actions = (r, l, u, d)
'''
import numpy as np
Q = [[{'r':0, 'd':0}, {'r':0, 'l':0, 'd':0}, {'l':0, 'd':0}],
     [{'r':0, 'u':0, 'd':0}, {'r':0, 'l':0, 'u':0, 'd':0}, {'l':0, 'u':0, 'd':0}],
     [{'u':0, 'r':0}, {'r':0, 'l':0, 'u':0}, {'l':0, 'u':0}]]

actions = {'r':(0, 1), 'd':(1, 0), 'u':(-1, 0), 'l':(0, -1)}

alpha = 0.1
g = 0.2

r = np.array([[1, -1, 1],
             [1, 1, 2],
             [1, -1, 1]])

def temporal(q, a, m, n):
    pos = (m, n)
    next_pos = tuple(map(lambda x, y:x+y, pos, actions[a]))
    row = next_pos[0]
    col = next_pos[1]
    temp = alpha*(r[row][col]+g*max(Q[row][col].values())-q)
    return temp

episodes = 8

for e in range(episodes):
    Q_copy = Q
    for i in range(3):
        for j in range(3):
            qv = Q_copy[i][j]
            for action in qv:
                qv[action] += temporal(qv[action], action, i, j)
    Q = Q_copy

res = []
for i in range(3):
    temp = []
    for j in range(3):
        dic = Q[i][j]
        temp.append((max(dic, key= lambda x: dic[x])))
    res.append(temp)

#It shows the best path to reach from S to E
print('\n\n')
for i in range(3):
    print(res[i])
print('\n\n')