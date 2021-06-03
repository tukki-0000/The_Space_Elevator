#インポート

import numpy as np

#初期設定

#地上を0mとする
m = 25 #kg　固定
g = 9.81 #m/s^2　固定

#関数

#接線力
def Tangential_Force(Torque, Radius):
    Tangential_Force = Torque / Radius
    return Tangential_Force

#加速度
def Acceleration(Tangential_Force):
    Acceleration = Tangential_Force / m - g
    return Acceleration




#のぼり（地上からの距離(Middle_H)からブレーキをかけた時）
print("のぼり")
v0 = float(input("v0[m/s]を入力してください"))
print("v0 =", v0, "[m/s]の時")
Middle_H = (v0 ** 2) / (2 * g)
print("Middle_H =", Middle_H)
print("")
Middle_H = float(input("頂点からの距離を入力してください"))
v0 = (Middle_H * 2 * g) ** (1 / 2)
print("Middle_H =", Middle_H,"[m]の時")
print("v0 = ", v0, "[m/s]")
