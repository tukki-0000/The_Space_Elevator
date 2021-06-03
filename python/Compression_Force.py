### タイヤ4つで実現できる摩擦力を求める ###
### 姫野くん 摩擦係数 ウレタン1.01 テザー0.2　21kg タイヤ4個　45℃　F=40N 先に決めたTcos45 = mg TA =57.8 ,TB = 39.2

#インポート

import math

#初期設定

m = 21 #[kg]
g = 9.81 #[m/s^2]
e = math.e

######## 関数群 ########

def TA(μ1, F, θ): #車輪の摩擦力入れる
    TA = 2 * μ1 * F * math.cos(math.radians(θ))
    return TA

def TB(μ2, F, θ): #テザーの摩擦入れる
    TB = e**(2*μ2*math.radians(θ)) * F * math.sin(math.radians(θ))
    return TB

def T_Last(n, θ, TA, TB):
    T_Last = (2*n - 1) * (TA + TB) * math.cos(math.radians(θ))
    return T_Last


######## MAIN #########

n = float(input("タイヤいくつ使う？")) / 2
θ = float(input("タイヤがなす角度[度]"))
F = float(input("全体（全て）の圧縮力[N]")) / n / 2
μ1 = float(input("車輪の摩擦係数(ウレタンだと1.01)を入力してください"))
μ2 = float(input("テザーの摩擦係数(0.2〜0.4くらい)を入力してください"))

TA1 = TA(μ1, F, θ)
TB1 = TB(μ2, F, θ)
T_Last1 = T_Last(n, θ, TA1, TB1)
print("TA =", TA1, "TB =", TB1, "T_Last =", T_Last1)

if T_Last1 > m * g:
    print("摩擦力で静止成功  上方向の力", T_Last1, "[N] > 重力" , m * g, "[N]")
else:
    print("摩擦力で静止失敗  上方向の力", T_Last1, "[N] < 重力" , m * g, "[N]")
