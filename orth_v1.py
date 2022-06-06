from math import sqrt
from matplotlib import pyplot as plt
def algorithm(matr,N,iterations_number):
    '''
    :param matr: матрица координат узлов
    :param N: размерность сетки NxN
    :param iterations_number: количество итераций
    :return:
    '''
    matr = creatematr(N)
    for i in range(0,iterations_number):
        construction(matr,N)
        ort=0
        for i in range(1, N - 1):
            for j in range(1, N - 1):
                d = matr[i][j]
                d1 = matr[i - 1][j]
                d2 = matr[i][j - 1]
                d3 = matr[i + 1][j]
                d4 = matr[i][j + 1]
                ort1 = (d[0] - d2[0]) * (d[0] - d3[0]) + (d[1] - d2[1]) * (d[1] - d3[1])
                ort2 = (d[0] - d1[0]) * (d[0] - d4[0]) + (d[1] - d1[1]) * (d[1] - d4[1])
                ort += (ort1 + ort2) / 2
        print('Ort',ort/(N-1)/(N-1))
    for r in range(1,iter+1):
       for i in range(1, N-1):
           matr[1][i] = ((matr[2][i][0] + matr[0][i][0])/2,(matr[2][i][1] + matr[0][i][1])/2)
    graph(matr,N)
    return matr

def distance(d1,d2):
    return (d2[0]-d1[0])*(d2[0]-d1[0])+(d2[1]-d1[1])*(d2[1]-d1[1])

def far(d0,d1,d2,d3,d4):
    dict  = {'1':d1,'2':d2,'3':d3,'4':d4}
    dist1 = distance(d0,d1)
    dist2 = distance(d0,d2)
    dist3 = distance(d0,d3)
    dist4 = distance(d0,d4)
    slovar2 = {'1':dist1,'2':dist2,'3':dist3,'4':dist4}
    dist = max(dist1, dist2, dist3, dist4)
    for j in dict:
        if slovar2[j]==dist:
            return dict[j]

def middle(d1,d2):
    x_mid = (d1[0]+d2[0])/2
    y_mid = (d1[1]+d2[1])/2
    return (x_mid,y_mid)

# функция для пересчёта точек на гипотенузе
def hypotenuse(node,node_below):
    old_node = node
    b = node_below[0]+node_below[1]
    x = b/2
    y = x
    node = (x,y)
    deviation = distance(node,old_node)
    return (node,deviation)

#по 4 точкам
def construction(matr,n):
                deviation = 0
                for i in range(1, n-1):
                    coords = matr[0][i]
                    d = matr[1][i]
                    b = d[0] + d[1]
                    x = b / 2
                    y = -x + b
                    matr[0][i] = (x, y)
                    deviation = deviation + distance(coords, matr[0][i])
                    for j in range(1, n-1):
                                coords = matr[i][j]
                                d1 = matr[i][j + 1]
                                d3 = matr[i][j - 1]
                                d4 = matr[i - 1][j]
                                d2 = matr[i + 1][j]
                                x1, y1 = d1[0], d1[1]
                                x2, y2 = d2[0], d2[1]
                                x3, y3 = d3[0], d3[1]
                                x4, y4 = d4[0], d4[1]
                                if (x1+x2-x3-x4)!=0:
                                    a = (y3 + y4 - y1 - y2) / (x1 + x2 - x3 - x4) #коэфицент a x=ay+b
                                    b = (y1 * y2 - y3 * y4 + x1 * x2 - x3 * x4) / (x1 + x2 - x3 - x4)  # коэфицент b x=ay+b
                                a2 = a * a + 1  # коэфицент a при поиске точки пересечения окружностей
                                b2 = 2 * a * b - a * x1 - a * x2 - y1 - y2  # коэфицент b при поиске точки пересечения окружностей
                                c2 = (x1 * x2 - b * x1 - b * x2 + y1 * y2 + b * b) # коэфицент c при поиске точки пересечения окружностей
                                if (b2 * b2 - 4 * a2 * c2 > 0):
                                    if a<0:
                                        y = (-b2 - sqrt(b2 * b2 - 4 * a2 * c2)) / 2 / a2
                                    else:
                                        y = (-b2 + sqrt(b2 * b2 - 4 * a2 * c2)) / 2 / a2
                                else:
                                    y = coords[1]
                                x = a * y + b
                                new_dot = (x, y)
                                far_dot = far(new_dot,d1,d2,d3,d4)
                                if far_dot == d1 or far_dot == d3:
                                    middle_dot = middle(d1, d3)
                                elif far_dot == d2 or far_dot == d4:
                                    middle_dot = middle(d2, d4)
                                new_new_dot = middle(new_dot, middle_dot)
                                x = new_new_dot[0]
                                y = new_new_dot[1]
                                if ((x > d3[0] and x < d1[0]) and (y > d2[1] and y < d4[1])):
                                    matr[i][j] = new_new_dot
                                    deviation = deviation + distance(coords, matr[i][j])
                #print(deviation)



def printmatr(matr):
        for i in range(0,len(matr)):
            for j in range(0, len(matr)):
                matr[i][j] = (round(matr[i][j][0], 10),round(matr[i][j][1], 10))
            print(matr[i])

def creatematr(n):
    matrix = []
    for i in range(0,n):
        matrix.append([])
        for j in range(0,n):
            matrix[i].append([j/(n-1),j/(n-1)*i/(n-1)])
    matrix = matrix[::-1]
    return matrix

# построение графика
def graph(matr,N):
    x = []
    y = []
    for i in range(0, N):
        for j in range(0, N):
            x.append(matr[i][j][0])
            y.append(matr[i][j][1])
    plt.scatter(x, y, marker=".", linewidths=0.05)
    for i in range(0, N):
        plt.plot(x[i * N:(i + 1) * N], y[i * N:(i + 1) * N], color='b', linewidth=0.5)
    for i in range(0, N):
        xx = []
        yy = []
        for j in range(0, N):
            xx.append(matr[j][i][0])
            yy.append(matr[j][i][1])
        plt.plot(xx, yy, color='b', linewidth=0.5)
    plt.show()

N =20
iter =1000
matr = []
matr = algorithm(matr,N,iter)
#matr =creatematr(N)

#for L in range(1,iter+1):
#        construction(matr,N)
#for r in range(1,iter+1):
#    dev = 0
#    for i in range(1, N-1):
#        matr[1][i] = ((matr[2][i][0] + matr[0][i][0])/2,(matr[2][i][1] + matr[0][i][1])/2)

