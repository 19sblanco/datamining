from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
import numpy as np


def get_error(model, x, y):
    n = len(x)
    sum = 0
    for i in range(n):
        pred = model.predict([x[i]])[0]
        diff = y[i] - pred
        sum += diff**2
    return sum * 0.5

def one_a_b(X_train, X_test, y_train, y_test):
    reg = LinearRegression()
    reg.fit(X_train, y_train)

    error = get_error(reg, X_train, y_train)
    print("train", error)
    print()
    error = get_error(reg, X_test, y_test)
    print("test", error)


def one_c_b(X_train, X_test, y_train, y_test):
    poly = PolynomialFeatures()
    X_train_transform = poly.fit_transform(X_train)
    X_test_transform = poly.fit_transform(X_test)

    reg = LinearRegression()
    reg.fit(X_train_transform, y_train)

    # print("coef", reg.coef_)
    # print("intercept", reg.intercept_)

    error = get_error(reg, X_train_transform, y_train)
    print("train_transform", error)
    print()
    error = get_error(reg, X_test_transform, y_test)
    print("test_transform", error)


def one_e(X_train, X_test, y_train, y_test):
    alphas = [0, 0.001, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 1, 10]
    for alpha in alphas:
        poly = PolynomialFeatures()
        X_train_transform = poly.fit_transform(X_train)
        X_test_transform = poly.fit_transform(X_test)

        reg = LinearRegression()
        reg.fit(X_train_transform, y_train)

        
        clf = Ridge(alpha=alpha)











    


def main():
    X , y = load_diabetes ( return_X_y = True , as_frame = False )
    X_train , X_test , y_train , y_test = train_test_split (X ,y , test_size =0.2 , shuffle = False )

    # print("a, b")
    # one_a_b(X_train, X_test, y_train, y_test)
    # print("c")
    # one_c_d(X_train, X_test, y_train, y_test)
    one_e(X_train, X_test, y_train, y_test)




main()



