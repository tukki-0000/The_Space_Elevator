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

#接線力
def Tangential_Force(Torque, Radius):
    if Torque == 0:
        Tangential_Force = 0
    else:
        Tangential_Force = Torque / Radius
    return Tangential_Force

#目標速度になるまでの時間
def Target_Speed_Time(Target_Speed, Tangential_Force):
    Target_Speed_Time = Target_Speed / (Tangential_Force / m + g)
    return Target_Speed_Time

##### MAIN ######

#おり

Torque = float(input("トルク[N・m]を入力してください"))
Radius = float(input("回転半径[mm]を入力してください")) / 1000 #[m]になおす
Target_Speed = float(input("到達目標速度[m/s]を入力してください"))
Tangential_Force1 = Tangential_Force(Torque, Radius)
Target_Speed_Time1 = Target_Speed_Time(Target_Speed, Tangential_Force1)
print(Tangential_Force1)
print("目標速度になるまでの時間", Target_Speed_Time1, "[s]")
