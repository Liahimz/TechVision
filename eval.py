#!/usr/bin/python3

# файл evaluator.py
import sys
import numpy as np


def read_data(filename):
    data = []
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            data.append(line[:-1])
    return data


def Calc_func(P, V, Cord, t):
    x = P[0][0] * (Cord[0] + V[0] * t) \
        + P[0][1] * (Cord[1] + V[1] * t) \
        + P[0][2] * (Cord[2] + V[2] * t) + P[0][3]

    c = P[2][0] * (Cord[0] + V[0] * t) \
        + P[2][1] * (Cord[1] + V[1] * t) \
        + P[2][2] * (Cord[2] + V[2] * t) + P[2][3]

    y = P[1][0] * (Cord[0] + V[0] * t) \
        + P[1][1] * (Cord[1] + V[1] * t) \
        + P[1][2] * (Cord[2] + V[2] * t) + P[1][3]


    # print(x)
    # print(y)
    # print(c)

    return x/(c + 1e-25), y/(c + 1e-25)

def Calc_func2(correct, P, V, Cord, t):
    x = P[0][0] * (Cord[0] + V[0] * t) \
        + P[0][1] * (Cord[1] + V[1] * t) \
        + P[0][2] * (Cord[2] + V[2] * t) + P[0][3]

    c = P[2][0] * (Cord[0] + V[0] * t) \
        + P[2][1] * (Cord[1] + V[1] * t) \
        + P[2][2] * (Cord[2] + V[2] * t) + P[2][3]

    y = P[1][0] * (Cord[0] + V[0] * t) \
        + P[1][1] * (Cord[1] + V[1] * t) \
        + P[1][2] * (Cord[2] + V[2] * t) + P[1][3]
    

    x_abs = np.abs(x - c * correct[0])

    y_abs = np.abs(y - c * correct[1])

    return x_abs + y_abs


def penalty(correct, P, V, Cord, t):
    # x, y = Calc_func(P, V, Cord, t)

    f = Calc_func2(correct, P, V, Cord, t)

    # return np.abs(x - correct[0]) + np.abs(y - correct[1])
    return f


if __name__ == '__main__':
    F = 0.0
    # считываем коэффициенты из sys.argv[1]
    a = list(map(float, list(open(sys.argv[1], 'r'))[0].split()))

    P = np.array([[a[0], a[1], a[2], a[3]], [a[4], a[5], a[6], a[7]], [a[8], a[9], a[10], a[11]]])
    V = np.array([a[12], a[13], a[14]])

    X_a = np.array([a[15], a[16], a[17]])
    X_e = np.array([a[18], a[19], a[20]])
    X_j = np.array([a[21], a[22], a[23]])

    data_x = read_data("/home/michael/Desktop/TechVision/x_2d.txt")
    data_y = read_data("/home/michael/Desktop/TechVision/y_2d.txt")

    lenght = int(len(data_x) / 3)
    
    # вычисляем функционал по обучающей базе
    
    # for line in base:
    #     line = line.strip().split()
    #     correct = line[0]
    #     f = map(float, line[1:])
    #     F += penalty(correct, f, a)

    for t in range(lenght):
        correct_a = [float(data_x[3 * t]), float(data_y[3 * t])]
        F += penalty(correct_a, P, V, X_a, t)
        correct_e = [float(data_x[3 * t + 1]), float(data_y[3 * t + 1])]
        F += penalty(correct_e, P, V, X_e, t)
        correct_j = [float(data_x[3 * t + 2]), float(data_y[3 * t + 2])]
        F += penalty(correct_j, P, V, X_j, t)

    # выводим значение функционала
    print(F)