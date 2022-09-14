def orderCars(cars):
    cars_T = []
    cars5 = []
    cars6 = []
    cars7 = []
    cars8 = []
    for car in cars:
        if car.events[len(car.events) - 2] == 'Ta37' or car.events[len(car.events) - 2] == 'Ta17':
            cars7.append(car)
        if car.events[len(car.events) - 2] == 'Tb36' or car.events[len(car.events) - 2] == 'Tb16':
            cars6.append(car)
        if car.events[len(car.events) - 2] == 'Tc38' or car.events[len(car.events) - 2] == 'Tc18':
            cars8.append(car)
        if car.events[len(car.events) - 2] == 'Td35' or car.events[len(car.events) - 2] == 'Td15':
            cars5.append(car)
    bigOrdery(cars5,cars_T)
    smallOrdery(cars6,cars_T)
    bigOrderx(cars8, cars_T)
    smallOrderx(cars7,cars_T)

    return cars_T


def bigOrdery(cars, cars_T):
    i = 0
    max = 0
    while len(cars) != 0:
        if len(cars) > 1:
            if cars[i].rect.centery > cars[max].rect.centery:
                max = i
        else:
            cars_T.append(cars[max])
            break
        i += 1
        if i == len(cars):
            cars_T.append(cars[max])  # 加入cars中
            cars.pop(max)  # 从备选删除
            max = 0
            i = 0


def smallOrdery(cars, cars_T):
    i = 0
    max = 0
    while len(cars) != 0:
        if len(cars) > 1:
            if cars[i].rect.centery < cars[max].rect.centery:
                max = i
        else:
            cars_T.append(cars[max])
            break
        i += 1
        if i == len(cars):
            cars_T.append(cars[max])  # 加入cars中
            cars.pop(max)  # 从备选删除
            max = 0
            i = 0

def bigOrderx(cars, cars_T):
    i = 0
    max = 0
    while len(cars) != 0:
        if len(cars) > 1:
            if cars[i].rect.centerx > cars[max].rect.centerx:
                max = i
        else:
            cars_T.append(cars[max])
            break
        i += 1
        if i == len(cars):
            cars_T.append(cars[max])  # 加入cars中
            cars.pop(max)  # 从备选删除
            max = 0
            i = 0


def smallOrderx(cars, cars_T):
    i = 0
    max = 0
    while len(cars) != 0:
        if len(cars) > 1:
            if cars[i].rect.centerx < cars[max].rect.centerx:
                max = i
        else:
            cars_T.append(cars[max])
            break
        i += 1
        if i == len(cars):
            cars_T.append(cars[max])  # 加入cars中
            cars.pop(max)  # 从备选删除
            max = 0
            i = 0


def carLeave(cars):
    carsA17 = 0  # s r
    carsA37 = 0  # L

    carsC18 = 0
    carsC38 = 0

    carsB16 = 0
    carsB36 = 0

    carsD15 = 0
    carsD35 = 0

    interval = 90
    startLow = 322
    startHigh = 575
    offset = 90
    endLow = 0 - offset  # -60
    endHigh = 865 + offset  # 1000
    maxCars = 3
    for car in cars:
        if car.events[len(car.events) - 2] == 'Ta17' and carsA17 < maxCars:
            if car.rect.centerx <= startLow:
                car.targetStart = endLow
                car.targetStart = car.targetStart + carsA17 * interval
                carsA17 += 1
                car.leavemark = leave_c(car)

        elif car.events[len(car.events) - 2] == 'Ta37' and carsA37 < maxCars:
            if car.rect.centerx <= startLow:
                car.targetStart = endLow
                car.targetStart = car.targetStart + carsA37 * interval
                carsA37 += 1
                car.leavemark = leave_c(car)

        elif car.events[len(car.events) - 2] == 'Tc18' and carsC18 < maxCars:
            car.row = 90
            if car.rect.centerx >= 565:
                car.targetStart = endHigh
                car.targetStart = car.targetStart - carsC18 * interval
                carsC18 += 1
                car.leavemark = leave_c(car)

        elif car.events[len(car.events) - 2] == 'Tc38' and carsC38 < maxCars:
            car.row = 90
            if car.rect.centerx >= 565:
                car.targetStart = endHigh
                car.targetStart = car.targetStart - carsC38 * interval
                carsC38 += 1
                car.leavemark = leave_c(car)

        elif car.events[len(car.events) - 2] == 'Tb16' and carsB16 < maxCars:
            car.row = 0
            if car.rect.centery <= 332:
                car.targetStart = endLow
                car.targetStart = car.targetStart + carsB16 * interval
                carsB16 += 1
                car.leavemark = leave_c(car)

        elif car.events[len(car.events) - 2] == 'Tb36' and carsB36 < maxCars:
            car.row = 0
            if car.rect.centery <= 332:
                car.targetStart = endLow
                car.targetStart = car.targetStart + carsB36 * interval
                carsB36 += 1
                car.leavemark = leave_c(car)

        elif car.events[len(car.events) - 2] == 'Td15' and carsD15 < maxCars:
            car.row = 0
            if car.rect.centery >= startHigh:
                car.targetStart = endHigh
                car.targetStart = car.targetStart - carsD15 * interval
                carsD15 += 1
                car.leavemark = leave_c(car)

        elif car.events[len(car.events) - 2] == 'Td35' and carsD35 < maxCars:
            car.row = 0
            if car.rect.centery >= startHigh:
                car.targetStart = endHigh
                car.targetStart = car.targetStart - carsD35 * interval
                carsD35 += 1
                car.leavemark = leave_c(car)


def leave_c(car):
    offset = 90
    if car.events[len(car.events) - 2] == 'Ta37' or car.events[len(car.events) - 2] == 'Ta17':
        if car.rect.centerx - car.targetStart > 0:
            car.rect.centerx -= 1
        if car.rect.centerx == -90 + offset:
            return True
    if car.events[len(car.events) - 2] == 'Tb36' or car.events[len(car.events) - 2] == 'Tb16':
        if car.rect.centery - car.targetStart > 0:
            car.rect.centery -= 1
        # print(car.rect.centerx - car.targetStart)
        if car.rect.centery == -90 + offset:
            return True
    if car.events[len(car.events) - 2] == 'Tc38' or car.events[len(car.events) - 2] == 'Tc18':
        if car.rect.centerx - car.targetStart < 0:
            car.rect.centerx += 1
        if car.rect.centerx == 955 - offset:
            return True
    if car.events[len(car.events) - 2] == 'Td35' or car.events[len(car.events) - 2] == 'Td15':
        if car.rect.centery - car.targetStart < 0:
            car.rect.centery += 1
        if car.rect.centery == 955 - offset:
            return True

    return False