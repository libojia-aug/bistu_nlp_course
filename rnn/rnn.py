# -*- coding:utf-8 -*- 
import numpy as np

_ROWS = 50
_INFINITESIMAL = 0.00000001

def at_func(b, W, h_prev, U, x):
    return b + np.dot(W, h_prev) + np.dot(U, x)


def ht_func(at):
    return np.tanh(at)


def ot_func(c, V, h):
    return c + np.dot(V, h)


class RNN:

    def __init__(self, input_dim, hidden_nodes, output_dim):
        self.U = np.random.random([hidden_nodes, input_dim]) * 0.01
        self.b = np.random.random([hidden_nodes]) * 0.01

        self.W = np.random.random([hidden_nodes, hidden_nodes]) * 0.01

        self.V = np.random.random([output_dim, hidden_nodes]) * 0.01
        self.c = np.random.random([output_dim]) * 0.01

        self.h = np.random.random([hidden_nodes]) * 0.01
 
    def forward(self, x):
        #列
        T = x.shape[1]
        states = []
        output = []
        for i in range(T):
            if i == 0:
                at = at_func(self.b, self.W, self.h, self.U, x[:, i])
            else:
                at = at_func(self.b, self.W, states[i - 1], self.U, x[:, i])
            ht = ht_func(at)
            ot = ot_func(self.c, self.V, ht)
            states.append(ht)
            output.append(ot)
        return states, output

    def backword(self, x, y, h, output, lr=0.002):
        T = x.shape[1]
        dL_T = np.dot(np.transpose(self.V), output[-1] - y[:, -1])
        # loss = np.sum(-y[:, -1] * np.log(output[-1]))
        dL_ht = dL_T

        D_U = np.zeros_like(self.U)
        D_b = np.zeros_like(self.b)

        D_W = np.zeros_like(self.W)

        D_V = np.zeros_like(self.V)
        D_c = np.zeros_like(self.c)

        for t in range(T - 2, -1, -1):
            dQ = output[t] - y[:, t]

            dy = 1 - h[t] * h[t]
            dL_ht += np.dot(np.transpose(self.V), dQ)

            D_U += np.outer(dy * dL_ht, x[:, t])
            D_b += dy * dL_ht

            D_W += np.outer(dy * dL_ht, h[t - 1])

            D_V += np.outer(dQ, h[t])
            D_c += dQ

        for dparam in [D_V, D_c, D_U, D_b, D_W]:
            np.clip(dparam, -5, 5, out=dparam)

        self.U -= lr * D_U / np.sqrt(D_U * D_U + _INFINITESIMAL)
        self.b -= lr * D_b / np.sqrt(D_b * D_b + _INFINITESIMAL)

        self.W -= lr * D_W / np.sqrt(D_W * D_W + _INFINITESIMAL)

        self.V -= lr * D_V / np.sqrt(D_V * D_V + _INFINITESIMAL)
        self.c -= lr * D_c / np.sqrt(D_c * D_c + _INFINITESIMAL)

        self.h -= lr * dL_ht / np.sqrt(dL_ht * dL_ht + _INFINITESIMAL)

        return self.h

    def sample(self, x):
        h = self.h
        predict = []
        for i in range(9):
            at = at_func(self.b, self.W, h, self.U, x)
            ht = ht_func(at)
            ot = ot_func(self.c, self.V, ht)
            ynext = np.argmax(ot)
            predict.append(ynext)
            x = np.zeros_like(x)
            x[ynext] = 1
        return predict

# create sequences with 10 number in each sequence


def getrandomdata(nums):
    x = np.zeros([nums, 10, 10], dtype=float)
    y = np.zeros([nums, 10, 10], dtype=float)
    for i in range(nums):
        tmpi = np.random.randint(0, 9)
        for j in range(9):
            if tmpi < 9:
                x[i, tmpi, j], y[i, tmpi + 1, j] = 1.0, 1.0
                tmpi = tmpi + 1
            else:
                x[i, tmpi, j], y[i, 0, j] = 1.0, 1.0
                tmpi = 0
    return x, y


def test(nums):
    testx = np.zeros([nums, 10], dtype=float)
    for i in range(nums):
        tmpi = np.random.randint(0, 9)
        testx[i, tmpi] = 1
    for i in range(nums):
        print('the given start number:', np.argmax(testx[i]))
        print('the created numbers:   ', model.sample(testx[i]))

if __name__ == '__main__':
    # x0 = [0, 1, 2, 3, 4, 5, 6, 7, 8]--> y0 = [1, 2, 3, 4, 5, 6, 7, 8, 0],
    # x1 = [5, 6, 7, 8, 0, 1, 2, 3, 4]--> y1 = [6, 7, 8, 0, 1, 2, 3, 4, 5]
    model = RNN(10, 200, 10)
    epoches = 5
    smooth_loss = 0
    for ll in range(epoches):
        print('epoch i:', ll)
        x, y = getrandomdata(_ROWS)
        for i in range(_ROWS):
            # print x[i]
            h, output = model.forward(x[i])
            state = model.backword(x[i], y[i], h, output, lr=0.001)
        test(7)
