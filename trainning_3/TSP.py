import numpy as np
answer = []
def tsp(graph, v, currPos, n, count, cost):

    if (count == n and graph[currPos][0]):
        answer.append(cost + graph[currPos][0])
        return

    for i in range(n):
        if (v[i] == False and graph[currPos][i]):
            v[i] = True
            tsp(graph, v, i, n, count + 1,
                cost + graph[currPos][i])
            v[i] = False

if __name__ == '__main__':
    n,m = input().split(' ')
    n = int(n)
    m = int(m)
    graph = (np.ones((n,n),dtype=int) - np.eye(n,dtype=int))*1000
    for _ in range(m):
        i,j,c = input().split(' ')
        i = int(i)
        j = int(j)
        c = int(c)
        graph[i-1][j-1] = c
    v = [False for i in range(n)]
    v[0] = True
    tsp(graph, v, 0, n, 1, 0)
    answer = int(min(answer))
    print(answer)

# [[ 0, 10, 15, 20 ],
# [ 10, 0, 35, 25 ],
# [ 15, 35, 0, 30 ],
# [ 20, 25, 30, 0 ]]