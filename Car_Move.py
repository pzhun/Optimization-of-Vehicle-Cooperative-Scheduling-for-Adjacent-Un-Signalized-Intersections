import random
import numpy as np

speed = 1


def angle(vec1, vec2, deg=False):
    _angle = np.arctan2(np.abs(np.cross(vec1, vec2)), np.dot(vec1, vec2))
    if deg:
        _angle = np.rad2deg(_angle)
    return _angle


def getRow(P1, P2, car, plusMark=False):
    v1 = np.array((P2[0] - P1[0], P2[1] - P1[1]))
    v2 = np.array((0, 1))
    car.row = int(angle(v1, v2) * 180 / 3.14)
    if plusMark:
        car.row = -car.row


def action_c(car, event):
    # road 1
    flag = 5
    if event == 'TF1a1r':
        flag = _TF1a1r(car)
    elif event == 'TF1a1s':
        flag = _TF1a1s(car)
    elif event == 'TF1a2':
        flag = _TF1a2(car)

        # road 2
    elif event == 'TF2c1r':
        flag = _TF2c1r(car)
    elif event == 'TF2c1s':
        flag = _TF2c1s(car)
    elif event == 'TF2c2':
        flag = _TF2c2(car)

        # road 3
    elif event == 'TF3b1r':
        flag = _TF3b1r(car)
    elif event == 'TF3b1s':
        flag = _TF3b1s(car)
    elif event == 'TF3b2':
        flag = _TF3b2(car)

    # road 4
    elif event == 'TF4d1r':
        flag = _TF4d1r(car)
    elif event == 'TF4d1s':
        flag = _TF4d1s(car)
    elif event == 'TF4d2':
        flag = _TF4d2(car)

    elif event == 'TFa1a3':
        flag = _TFa1a3(car)
    elif event == 'TFc1c3':
        flag = _TFc1c3(car)
    elif event == 'TFd1d3':
        flag = _TFd1d3(car)
    elif event == 'TFb1b3':
        flag = _TFb1b3(car)

    elif event == 'TFa3d2':
        flag = _TFa3d2(car)
    elif event == 'TFc3b2':
        flag = _TFc3b2(car)
    elif event == 'TFd3c2':
        flag = _TFd3c2(car)
    elif event == 'TFb3a2':
        flag = _TFb3a2(car)

    elif event == 'TFd2d1':
        flag = _TFd2d1(car)
    elif event == 'TFb2b1':
        flag = _TFb2b1(car)
    elif event == 'TFc2c1':
        flag = _TFc2c1(car)
    elif event == 'TFa2a1':
        flag = _TFa2a1(car)

    elif event == 'TFa2a4':
        flag = _TFa2a4(car)
    elif event == 'TFc2c4':
        flag = _TFc2c4(car)
    elif event == 'TFb2b4':
        flag = _TFb2b4(car)
    elif event == 'TFd2d4':
        flag = _TFd2d4(car)

    elif event == 'TFa4b4':
        flag = _TFa4b4(car)
    elif event == 'TFc4d4':
        flag = _TFc4d4(car)
    elif event == 'TFb4c4':
        flag = _TFb4c4(car)
    elif event == 'TFd4a4':
        flag = _TFd4a4(car)

    elif event == 'TFb4c3':
        flag = _TFb4c3(car)
    elif event == 'TFd4a3':
        flag = _TFd4a3(car)
    elif event == 'TFc4d3':
        flag = _TFc4d3(car)
    elif event == 'TFa4b3':
        flag = _TFa4b3(car)

    return flag


# road 1
def _TF1a1r(car):
    if 340 >= car.rect.centery >= 200:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        if car.rect.centery > 340:
            car.rect.centery = 340
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
    else:
        return 1


def _TF1a1s(car):
    if 350 > car.rect.centery >= 200:
        if car.rect.centery == 200:
            car.floaty = float(car.rect.centery + 1)
        car.floaty += speed
        car.rect.centery = int(car.floaty)
    else:
        return 4  # 事件完成


def _TFa1a3(car):
    if 425 > car.rect.centery >= 350:
        car.floaty += speed
        car.rect.centery = int(car.floaty)
    else:
        return 2  # 事件完成


def _TFa3d2(car):
    if 500 > car.rect.centery >= 425:  # 未确认
        car.floaty += speed
        car.rect.centery = int(car.floaty)
    else:
        return 2  # 事件完成


def _TFd2d1(car):
    if 575 > car.rect.centery >= 500:  # 未确认
        car.floaty += speed
        car.rect.centery = int(car.floaty)
    else:
        return 2


def _TF1a2(car):
    if 345 > car.rect.centery >= 200:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # car.rect.centery += 1
    else:
        return 4  # 事件完成


def _TFa2a4(car):
    if 405 > car.rect.centery >= 345:
        # if car.rect.centery == 345:
        #     if car.waitingTime != 10:
        #         car.waitingTime += 1
        #         return 0

        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # if car.rect.centery < 370:
        #     car.rect.centery += 1
        #     return 0
        # else:
        #     car.rect.centery += 1
        #     car.rect.centerx += 1
        #     car.row = 45
    else:
        return 4  # 事件完成


def _TFa4b4(car):
    if 450 > car.rect.centery >= 405:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # car.rect.centery += 1
        # car.rect.centerx += 1
    return 0


def _TFb4c3(car):
    if 565 > car.rect.centerx >= 494:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # car.row = 90
        # if car.rect.centery < 490:
        #     car.rect.centery += 1
        #     car.row = 45
        # car.rect.centerx += 1

    else:
        return 2  # 事件完成


# road 2
def _TF2c1r(car):
    if 575 <= car.rect.centery <= 661:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        if car.rect.centery < 575:
            car.rect.centery = 575
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
    else:
        return 1
        # if car.rect.centery != 575:
        #     car.rect.centery -= 1
        # else:
        #     if 580 > car.rect.centerx >= 545:
        #         car.rotate(90)
        #         car.rect.centerx += 1
        #         return 3  # 事件未完成
        #     else:
        #         return 4  # 事件完成


def _TF2c1s(car):
    if 661 >= car.rect.centery > 558:
        if car.rect.centery == 661:
            car.floaty = float(car.rect.centery - 1)
        car.floaty -= speed
        car.rect.centery = int(car.floaty)
    else:
        return 4


def _TFc1c3(car):
    if 558 >= car.rect.centery > 485:
        car.floaty -= speed
        car.rect.centery = int(car.floaty)
    else:
        return 2


def _TFc3b2(car):
    if 485 >= car.rect.centery > 410:
        car.floaty -= speed
        car.rect.centery = int(car.floaty)
    else:
        return 2


def _TFb2b1(car):
    if 410 >= car.rect.centery > 332:
        car.floaty -= speed
        car.rect.centery = int(car.floaty)
    else:
        return 2


# goal = 4
def _TF2c2(car):
    if 661 >= car.rect.centery > 557:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
        # car.rect.centery -= 1
    else:
        return 4


def _TFc2c4(car):
    if 557 >= car.rect.centery > 485:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
        # if car.rect.centery > 530:
        #     car.rect.centery -= 1
        #     return 0
        # else:
        #     car.rotate(45)
        #     car.rect.centery -= 1
        #     car.rect.centerx -= 1
    else:
        return 4


def _TFc4d4(car):
    if 485 >= car.rect.centery > 435:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
        # car.rotate(45)
        # car.rect.centery -= 1
        # car.rect.centerx -= 1
    return 0


def _TFd4a3(car):
    if 393 >= car.rect.centerx > 322:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
        # car.rotate(90)
        # if car.rect.centery > 430:
        #     car.rect.centery -= 1
        #     car.rotate(45)
        # car.rect.centerx -= 1

    else:
        return 2  # 事件完成


# road 3
def _TF3b1r(car):
    if 545 <= car.rect.centerx <= 661:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        if car.rect.centerx < 565:
            car.rect.centerx = 565
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
    else:
        return 1
        # if car.rect.centerx != 565:
        #     car.rect.centerx -= 1
        # else:
        #     if 348 >= car.rect.centery > 280:
        #         car.rotate(0)
        #         car.rect.centery -= 1
        #         return 3  # 事件未完成
        #     else:
        #         return 4  # 事件完成


def _TF3b1s(car):
    if 661 >= car.rect.centerx > 550:
        if car.rect.centerx == 661:
            car.floatx = float(car.rect.centerx - 1)
        car.floatx -= speed
        car.rect.centerx = int(car.floatx)
    else:
        return 4


def _TFb1b3(car):
    if 550 >= car.rect.centerx > 472:
        car.floatx -= speed
        car.rect.centerx = int(car.floatx)
    else:
        return 2


def _TFb3a2(car):
    if 472 >= car.rect.centerx > 396:
        car.floatx -= speed
        car.rect.centerx = int(car.floatx)
    else:
        return 2


def _TFa2a1(car):
    if 396 >= car.rect.centerx > 322:
        car.floatx -= speed
        car.rect.centerx = int(car.floatx)
    else:
        return 2


def _TF3b2(car):
    if 661 >= car.rect.centerx > 548:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
        # car.rotate(90)
        # car.rect.centerx -= 1
    else:
        return 4


def _TFb2b4(car):
    if 548 >= car.rect.centerx > 483:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
        # if car.rect.centerx > 510:
        #     car.rotate(90)
        #     car.rect.centerx -= 1
        #     return 0
        # else:
        #     car.rotate(-45)
        #     car.rect.centery += 1
        #     car.rect.centerx -= 1
    else:
        return 4


def _TFb4c4(car):
    if 483 >= car.rect.centerx > 440:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
        # car.rotate(-45)
        # car.rect.centery += 1
        # car.rect.centerx -= 1
    return 0


def _TFc4d3(car):
    if 575 > car.rect.centery >= 495:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car, True)
        car.Point += 1
        # car.rotate(0)
        # if car.rect.centerx > 420:
        #     car.rect.centerx -= 1
        #     car.rotate(-45)
        # car.rect.centery += 1
    else:
        return 2  # 事件完成


# road 4
def _TF4d1r(car):
    if 340 >= car.rect.centerx >= 200:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # if car.rect.centerx != 340:
        #     car.rect.centerx += 1
        # else:
        #     if 600 > car.rect.centery >= 545:
        #         car.rotate(0)
        #         car.rect.centery += 1
        #         return 3  # 事件未完成
        #     else:
        #         return 4  # 事件完成


def _TF4d1s(car):
    if 340 > car.rect.centerx >= 200:
        if car.rect.centerx == 200:
            car.floatx = float(car.rect.centerx + 1)
        car.floatx += speed
        car.rect.centerx = int(car.floatx)
    else:
        return 4  # 事件完成


def _TFd1d3(car):
    if 414 > car.rect.centerx >= 340:
        car.floatx += speed
        car.rect.centerx = int(car.floatx)
    else:
        return 2  # 事件完成


def _TFd3c2(car):
    if 488 > car.rect.centerx >= 414:
        car.floatx += speed
        car.rect.centerx = int(car.floatx)
    else:
        return 2  # 事件完成


def _TFc2c1(car):
    if 565 > car.rect.centerx >= 488:
        car.floatx += speed
        car.rect.centerx = int(car.floatx)
    else:
        return 2


def _TF4d2(car):
    if 338 > car.rect.centerx >= 200:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # car.rect.centerx += 1
        # car.rotate(90)
    else:
        return 4  # 事件完成


def _TFd2d4(car):
    if 402 > car.rect.centerx >= 338:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # if car.rect.centerx < 355:
        #     car.rect.centerx += 1
        #     return 0
        # else:
        #     car.rect.centery -= 1
        #     car.rect.centerx += 1
        #     car.rotate(-45)
    else:
        return 4  # 事件完成


def _TFd4a4(car):
    if 450 > car.rect.centerx >= 402:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # car.rotate(-45)
        # car.rect.centery -= 1
        # car.rect.centerx += 1
    return 0


def _TFa4b3(car):
    if 406 >= car.rect.centery > 332:
        car.rect.centery = car.PathPoints[car.Point][1]
        car.rect.centerx = car.PathPoints[car.Point][0]
        getRow(car.PathPoints[car.Point - 1], car.PathPoints[car.Point], car)
        car.Point += 1
        # car.rotate(0)
        # if car.rect.centerx < 490:
        #     car.rect.centerx += 1
        #     car.rotate(-45)
        # car.rect.centery -= 1
    else:
        return 2  # 事件完成


def leave_c(car):
    if car.events[len(car.events) - 2] == 'Ta37' or car.events[len(car.events) - 2] == 'Ta17':
        car.rect.centerx -= 1
        if car.rect.centerx == -60:
            return True
    if car.events[len(car.events) - 2] == 'Tb36' or car.events[len(car.events) - 2] == 'Tb16':
        car.rect.centery -= 1
        # print(car.rect.centery)
        if car.rect.centery == -60:
            return True
    if car.events[len(car.events) - 2] == 'Tc38' or car.events[len(car.events) - 2] == 'Tc18':
        car.rect.centerx += 1
        if car.rect.centerx == 1000:
            return True
    if car.events[len(car.events) - 2] == 'Td35' or car.events[len(car.events) - 2] == 'Td15':
        car.rect.centery += 1
        if car.rect.centery == 1000:
            return True

    return False


def cardel(cars, loop, muitMark, inter):
    i = 0
    leaveCars = 0
    while i < len(cars):
        if cars[i].leavemark and loop % inter == 0:
            if muitMark:
                if leaveProbability():
                    cars.pop(i)
                    leaveCars += 1
            else:
                cars.pop(i)
                leaveCars += 1
        elif cars[i].rect.centerx < 0 and cars[i].curevent > 3:
            cars.pop(i)
            leaveCars += 1
        elif cars[i].rect.centerx > 955 - 90 and cars[i].curevent > 3:
            cars.pop(i)
            leaveCars += 1
        elif cars[i].rect.centery < 0 and cars[i].curevent > 3:
            cars.pop(i)
            leaveCars += 1
        elif cars[i].rect.centery > 955 - 90 and cars[i].curevent > 3:
            cars.pop(i)
            leaveCars += 1
        else:
            i += 1

    return leaveCars


def delCarsIntersection(cars):
    sum = 0
    for car in cars:
        if car.events[car.curevent] == "out":
            sum += 1
    if sum == len(cars):
        return True  # 意味着 所有车辆已经驶离交叉口。
    else:
        return False


def delCarsFast(cars, carsIntersection):
    i = 0
    leaveCars = 0
    TLeave = ['Ta17', 'Tb16', 'Tc18', 'Td15', 'Ta37', 'Tb36', 'Tc38', 'Td35', 'out']
    while i < len(carsIntersection):
        # print(carsIntersection[i].events[carsIntersection[i].curevent])
        if carsIntersection[i].events[carsIntersection[i].curevent] in TLeave:
            carsIntersection.pop(i)
        else:
            i += 1
    i = 0
    while i < len(cars):
        # print(cars[i].events[cars[i].curevent])
        # print(cars[i].rect.centerx,cars[i].rect.centery)
        if cars[i].events[cars[i].curevent] in TLeave:
            cars.pop(i)
            leaveCars += 1
        else:
            i += 1
    return leaveCars


def leaveProbability():
    r = random.randint(1, 100)
    if r < 60:
        # print(True)
        return True
    else:
        # print(False)
        return False


def action(car, event):
    flag = 10
    if event == 'T1a1r':
        flag = _TF1a1r(car)
    elif event == 'T1a1s':
        flag = _TF1a1s(car)
    elif event == 'T1a2':
        flag = _TF1a2(car)

        # road 2
    elif event == 'T2c1r':
        flag = _TF2c1r(car)
    elif event == 'T2c1s':
        flag = _TF2c1s(car)
    elif event == 'T2c2':
        flag = _TF2c2(car)

        # road 3
    elif event == 'T3b1r':
        flag = _TF3b1r(car)
    elif event == 'T3b1s':
        flag = _TF3b1s(car)
    elif event == 'T3b2':
        flag = _TF3b2(car)

    # road 4
    elif event == 'T4d1r':
        flag = _TF4d1r(car)
    elif event == 'T4d1s':
        flag = _TF4d1s(car)
    elif event == 'T4d2':
        flag = _TF4d2(car)

    elif event == 'Ta1a3':
        flag = _TFa1a3(car)
    elif event == 'Tb1b3':
        flag = _TFb1b3(car)
    elif event == 'Tc1c3':
        flag = _TFc1c3(car)
    elif event == 'Td1d3':
        flag = _TFd1d3(car)

    elif event == 'Ta3d2':
        flag = _TFa3d2(car)
    elif event == 'Tb3a2':
        flag = _TFb3a2(car)
    elif event == 'Tc3b2':
        flag = _TFc3b2(car)
    elif event == 'Td3c2':
        flag = _TFd3c2(car)

    elif event == 'Td2d1':
        flag = _TFd2d1(car)
    elif event == 'Ta2a1':
        flag = _TFa2a1(car)
    elif event == 'Tb2b1':
        flag = _TFb2b1(car)
    elif event == 'Tc2c1':
        flag = _TFc2c1(car)

    elif event == 'Ta2a4':
        flag = _TFa2a4(car)
    elif event == 'Tb4c3':
        flag = _TFb4c3(car)

    elif event == 'Tc2c4':
        flag = _TFc2c4(car)
    elif event == 'Td4a3':
        flag = _TFd4a3(car)

    elif event == 'Tb2b4':
        flag = _TFb2b4(car)
    elif event == 'Tc4d3':
        flag = _TFc4d3(car)

    elif event == 'Td2d4':
        flag = _TFd2d4(car)
    elif event == 'Ta4b3':
        flag = _TFa4b3(car)

    elif event == 'Ta4b4':
        flag = _TFa4b4(car)
    elif event == 'Tc4d4':
        flag = _TFc4d4(car)
    elif event == 'Tb4c4':
        flag = _TFb4c4(car)
    elif event == 'Td4a4':
        flag = _TFd4a4(car)

    return flag
