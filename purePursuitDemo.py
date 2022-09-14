import numpy as np
import math
import matplotlib.pyplot as plt
import pickle
import xlwt
import xlrd

# 定义常数
k = 0.1  # look forward gain
Lfc = 20.0  # look-ahead distance
Kp = 1.0  # speed propotional gain
dt = 0.1  # [s]
L = 2.9  # [m] wheel base of vehicle

show_animation = True


class VehicleState:  # 定义一个类，用于调用车辆状态信息

    def __init__(self, x=0.0, y=0.0, yaw=0.0, v=0.0):
        self.x = x
        self.y = y
        self.yaw = yaw
        self.v = v


def update(state, a, delta):  # 更新车辆状态信息

    state.x = state.x + state.v * math.cos(state.yaw) * dt
    state.y = state.y + state.v * math.sin(state.yaw) * dt
    state.yaw = state.yaw + state.v / L * math.tan(delta) * dt
    state.v = state.v + a * dt

    return state


def PIDControl(target, current):  # PID控制，定速巡航
    a = Kp * (target - current)

    return a


def pure_pursuit_control(state, cx, cy, pind):  # 纯跟踪控制器

    ind = calc_target_index(state, cx, cy)  # 找到最近点的函数，输出最近点位置

    if pind >= ind:
        ind = pind

    if ind < len(cx):
        tx = cx[ind]
        ty = cy[ind]
    else:
        tx = cx[-1]
        ty = cy[-1]
        ind = len(cx) - 1

    alpha = math.atan2(ty - state.y, tx - state.x) - state.yaw

    if state.v < 0:  # 如果是倒车的话，就要反过来
        alpha = math.pi - alpha

    Lf = k * state.v + Lfc

    delta = math.atan2(2.0 * L * math.sin(alpha) / Lf, 1.0)  # 核心计算公式

    return delta, ind


def calc_target_index(state, cx, cy):
    # 找到与车辆当前位置最近点的序号

    # search nearest point index
    dx = [state.x - icx for icx in cx]
    dy = [state.y - icy for icy in cy]
    d = [abs(math.sqrt(idx ** 2 + idy ** 2)) for (idx, idy) in zip(dx, dy)]
    ind = d.index(min(d))
    L = 0.0

    Lf = k * state.v + Lfc
    if ind < 340:
        return 340

    # search look ahead target point index
    # while Lf > L and (ind + 1) < len(cx):
    #     dx = cx[ind + 1] - cx[ind]
    #     dy = cx[ind + 1] - cx[ind]
    #     L += math.sqrt(dx ** 2 + dy ** 2)
    #     ind += 1

    # if 380 <= ind < 408 or ind == 727:
    #     ind = 408

    # if ind == len(cx)-1:
    #     return len(cx)-200
    Lf = Lfc
    while L < Lf and (ind + 1) < len(cx):
        ind += 1
        L += 1
    if 390 <= ind < 430:
        ind = 430
    return ind


def main():
    #  target course ，随机出来一条sin函数曲线
    Goal = 4

    xls = xlrd.open_workbook('./excel/target/targetLineGoal=' + str(Goal) + '.xls', formatting_info=True)
    sheet = xls.sheet_by_name("My Worksheet")
    cx_T = sheet.col_values(0, start_rowx=1, end_rowx=900)
    cy_T = sheet.col_values(1, start_rowx=1, end_rowx=900)
    cx = []
    cy = []
    for i in range(0, len(cx_T)):
        cx.append(float(cx_T[i]))
        cy.append(float(cy_T[i]))

    target_speed = 10.0 / 3.6  # [m/s]

    T = 200.0  # max simulation time

    # initial state
    state = VehicleState(x=cx[200], y=cy[200], yaw=-90 * 3.14 / 180, v=0.0)

    lastIndex = len(cx) - 1
    time = 0.0
    x = [state.x]
    y = [state.y]
    yaw = [state.yaw]
    v = [state.v]
    t = [0.0]
    target_ind = calc_target_index(state, cx, cy)
    # target_ind = 110
    print(target_ind)
    # 不断执行更新操作
    PathPoints = []
    index = 1
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('My Worksheet')
    worksheet.write(0, 0, "x")
    worksheet.write(0, 1, "y")
    worksheet.write(0, 2, "yaw")

    while T >= time and lastIndex > target_ind:

        ai = PIDControl(target_speed, state.v)
        di, target_ind = pure_pursuit_control(state, cx, cy, target_ind)
        state = update(state, ai, di)
        # print(target_ind)
        time = time + dt

        x.append(state.x)
        y.append(state.y)
        yaw.append(state.yaw)
        v.append(state.v)
        t.append(time)

        PathPoints.append([state.x, state.y, state.yaw])

        # print(x)
        # print(y)
        worksheet.write(index, 0, state.x)
        worksheet.write(index, 1, state.y)
        worksheet.write(index, 2, state.yaw)
        index += 1
        print(T, time, lastIndex, target_ind)
        if show_animation:
            plt.cla()
            plt.plot(cx, cy, ".r", label="course")
            plt.plot(x, y, "-b", label="trajectory")
            plt.plot(cx[target_ind], cy[target_ind], "xg", label="target")
            plt.axis("equal")
            plt.grid(True)
            plt.title("Speed[km/h]:" + str(state.v * 3.6)[:4])
            plt.pause(0.001)
            # plt.show()

    file = open('./data/PathPointsGoal=' + str(Goal) + '.pkl', 'wb')
    pickle.dump(PathPoints, file)
    file.close()
    workbook.save('./excel/goal=' + str(Goal) + '.xls')
    # print(x)
    # print(y)
    # print(yaw)


if __name__ == '__main__':
    print("Pure pursuit path tracking simulation start")
    main()
