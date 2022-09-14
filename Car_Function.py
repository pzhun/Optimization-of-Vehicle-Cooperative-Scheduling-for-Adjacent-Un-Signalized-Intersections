import pygame
import operation as op
import Car_Move as CM
import Car_position2marking as p2m


def update_screen(ai_settings, screen, intersection, cars):
    screen.fill(ai_settings.bg_color)  # 绘制屏幕
    intersection.blitme()  # 展示交叉口
    for car in cars:
        car.LINES_LIST.append((car.rect.centerx, car.rect.centery))
        # car.LINES_LIST = car.LINES_LIST[-100:-1]
        # print(car.LINES_LIST)
        pygame.draw.lines(screen, car.lineColor, 0, car.LINES_LIST,width=2  )
        car.blitme()
    pygame.display.flip()  # 让最近绘制的屏幕可见


def car_leave(car):
    if 'a7r' in car.events or 'a7l' in car.events or 'a7s' in car.events:
        if car.rect.centerx <= 83:
            car.rect.centerx -= 1

    if 'b6r' in car.events or 'b6l' in car.events or 'b6s' in car.events:
        if car.rect.centery <= 83:
            car.rect.centery -= 1

    if 'c8r' in car.events or 'c8l' in car.events or 'c8s' in car.events:
        if car.rect.centerx >= 826:
            car.rect.centerx += 1

    if 'd5r' in car.events or 'd5l' in car.events or 'd5s' in car.events:
        if car.rect.centery >= 826:
            car.rect.centery += 1


def opt2action2(Cars, PN):
    for car in Cars:  # 车辆有其对应的事件 且为瞬时事件
        event = car.events[car.curevent]
        # if car.name == 5 and event == "Td1d3":
        #     node = findNode(PN,event)
        #     if op.canhappenStrict(PN, node):
        #         print(000)
        node = findNode(PN, event)
        if node != None:
            if 'F' not in event:
                if op.canhappenStrict(PN, node):
                    op.transition(node)
                    CM.action(car, event)
                    car.curevent += 1
            else:
                if op.canhappen(node):
                    CM.action_c(car, event)
            # p2m.position2marking(PN, Cars)


def prioritySection(cars, carsWait):
    carsWait_T = []
    pSections = []
    for car in cars:
        event = car.events[car.curevent]
        # print(event)
        if 'F' not in event:
            pSection = event[3:5]
            pSections.append(pSection)
        else:
            event = car.events[car.curevent + 1]
            if event != "out":
                pSection = event[3:5]
                pSections.append(pSection)
    # print(pSections)
    for car in carsWait:
        event = car.events[car.curevent]
        if 'F' not in event:
            pSection = event[2:4]
            if pSection not in pSections:
                carsWait_T.append(car)

    return carsWait_T


def carController(car, PN, isMuit, MAX):  # true进 false不动
    Mpre = op.CurM(PN)
    event = car.events[car.curevent]
    if isMuit and car.curevent <= 1:
        if roadController(PN, car, MAX):
            return False

    return pController(PN, event, Mpre)


def roadController(PN, car, max):
    MAX = max
    # print(PN.carNums)
    if car.events[len(car.events) - 2] == 'Td15' and PN.carNums[0] > MAX:
        return True
    elif car.events[len(car.events) - 2] == 'Td35' and PN.carNums[1] > MAX:
        return True
    elif car.events[len(car.events) - 2] == 'Tb16' and PN.carNums[2] > MAX:
        return True
    elif car.events[len(car.events) - 2] == 'Tb36' and PN.carNums[3] > MAX:
        return True
    elif car.events[len(car.events) - 2] == 'Ta17' and PN.carNums[4] > MAX:
        return True
    elif car.events[len(car.events) - 2] == 'Ta37' and PN.carNums[5] > MAX:
        return True
    elif car.events[len(car.events) - 2] == 'Tc18' and PN.carNums[6] > MAX:
        return True
    elif car.events[len(car.events) - 2] == 'Tc38' and PN.carNums[7] > MAX:
        return True
    else:
        return False


def pController(PN, event, Mpre):
    ANodes = ['T1l', 'T2l', 'T3l', 'T4l', 'T1r', 'T2r', 'T3r', 'T4r', 'T1s', 'T2s', 'T3s', 'T4s']
    LNodes = ['T1a2', 'T2c2', 'T3b2', 'T4d2']
    if event in ANodes:
        return True
    node = findNode(PN, event)
    if event in LNodes:
        if additionalControl(event, PN):
            return False

    if node in PN.Tleave:
        return True
    if op.canhappen(node):  # 是否能够发生
        op.transition(node)
        if op.isdead(PN, Mpre):  # 发生后是否死锁，死锁则true
            return False
        else:
            return True
    else:
        return False


def additionalControl(event, PN):
    a4 = 0
    b4 = 0
    c4 = 0
    d4 = 0
    if PN.Pa4.token == 0 or PN.P1a2.token + PN.Pwa2a4.token >= 1:
        a4 = 1
    if PN.Pb4.token == 0 or PN.P3b2.token + PN.Pwb2b4.token >= 1:
        b4 = 1
    if PN.Pc4.token == 0 or PN.P2c2.token + PN.Pwc2c4.token >= 1:
        c4 = 1
    if PN.Pd4.token == 0 or PN.P4d2.token + PN.Pwd2d4.token >= 1:
        d4 = 1

    if event == 'T1a2' and b4 + c4 + d4 >= 3:
        return True
    if event == 'T2c2' and a4 + b4 + d4 >= 3:
        return True
    if event == 'T3b2' and a4 + c4 + d4 >= 3:
        return True
    if event == 'T4d2' and a4 + b4 + c4 >= 3:
        return True


# if PN.Pwa4b4.token== 1  and PN.Pwc4d4.token== 1 and PN.Pwb4c4.token== 1 and PN.Pwd2d4.token == 1 and PN.Pwa3d2.token== 1:
#     writeM(M, PN)
#     return True
# if PN.Pwa4b4.token == 1 and PN.Pwc4d4.token == 1 and PN.Pwb2b4.token == 1and PN.Pwd4a4.token == 1 and PN.Pwc3b2.token== 1:
#     writeM(M, PN)
#     return True
# if PN.Pwa4b4.token == 1 and PN.Pwc2c4.token == 1 and PN.Pwb4c4.token == 1 and PN.Pwd4a4.token == 1 and PN.Pwd3c2.token== 1:
#     writeM(M, PN)
#     return True
# if PN.Pwa2a4.token == 1  and PN.Pwb3a2.token== 1:
#     writeM(M, PN)
#     return True

def controller(PN, cars_T, cars, muitMark, MAX):
    for car in cars_T:  # 先让内部车走
        moveMark = carController(car, PN, muitMark, MAX)
        if moveMark:
            cars.append(car)
            event = car.events[car.curevent]
            for node in PN.Nodes:  # 找到PN中对应的事件，如果可以发生 让其发生
                if node.name == event:
                    op.transition(node)


def findNode(PN, event):
    for node in PN.Nodes:  # 找到PN中对应的事件，如果可以发生 让其发生
        if node.name == event:
            return node


def eventControl(PN):
    optSequence = []
    for node in PN.intersectionNodes:
        if node.token >= 1 and op.canhappenStrict(PN, node.next[0]):
            op.transition(node.next[0])
            optSequence.append(node.next[0].name)
    for node in PN.waitNodes:
        if node.token >= 1 and op.canhappenStrict(PN, node.next[0]):
            op.transition(node.next[0])
            optSequence.append(node.next[0].name)
    return optSequence


def activeCars(cars, opt):
    TLeave = ['Ta17', 'Tb16', 'Tc18', 'Td15', 'Ta37', 'Tb36', 'Tc38', 'Td35', 'out']
    actCars = []
    for event in opt:
        for car in cars:
            if car.events[car.curevent] in TLeave:
                actCars.append(car)
                break
            if event == car.events[car.curevent]:
                actCars.append(car)
                break

    return actCars


def leftTurnAdjust(cars):
    cars_T = []
    abMark = False
    _4dCar = None
    bcMark = False
    _1aCar = None
    cdMark = False
    _2bCar = None
    daMark = False
    _3cCar = None

    for car in cars:
        if car.goal == 1:  # 1a2
            if 404 < car.rect.centery < 428:
                abMark = True
                # print("active")
        if car.goal == 4:  # 2c2
            if 465 < car.rect.centery < 486:
                cdMark = True

        if car.goal == 7:  # 3b2
            if 465 < car.rect.centerx < 484:
                bcMark = True

        if car.goal == 10:  # 4d2
            if 401 < car.rect.centerx < 425:
                daMark = True
                # print("active")
    for car in cars:
        addMark = True
        if car.curevent == 5:
            if car.goal == 10 and abMark:
                addMark = False
            elif car.goal == 1 and bcMark:
                addMark = False
            elif car.goal == 7 and cdMark:
                addMark = False
            elif car.goal == 4 and daMark:
                addMark = False
        if addMark:
            cars_T.append(car)

    return cars_T