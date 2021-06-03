#インポート

import numpy as np

#初期設定

#地上を0mとする
m = 25 #kg　固定
g = 9.81 #m/s^2　固定

#関数

#位置エネルギー
def Potential_Energy(m, h):
    Potential_Energy = m * g * h
    return Potential_Energy

#運動エネルギー
def Kinetic_Energy(m, v):
    Kinetic_Energy = 1/2 * m * (v ** 2)
    return Kinetic_Energy


#おり（頂上からの距離(Middle_H = 10 ~ 30[m])からブレーキをかけた時）
print("おり")

v = float(input("ブレーキをかける瞬間のv[m/s]を入力してください"))
Middle_H = float(input("何m手前でブレーキをかけますか？"))

Middle_Potential_Energy = Potential_Energy(m, Middle_H) #地上からの距離Middle_H
Middle_Kinetic_Energy = Kinetic_Energy(m, v) #5~8m/s

Friction_Energy = (Middle_Potential_Energy + Middle_Kinetic_Energy)

#この摩擦エネルギーに地上からの距離(最高点 - 途中の距離[m])を割ると摩擦力が出てくる
#摩擦力 Friction
Friction = Friction_Energy / Middle_H


print("v =", v, "[m/s] Middle_H =", Middle_H, "[m]")
print("摩擦力", Friction, "[N]", Friction * 0.102, "[kgf]")
