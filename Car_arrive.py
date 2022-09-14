def carArrive(cars):
    carsA1 = 0
    carsA2 = 0
    carPreA1 = 0
    carPreA2 = 0

    carsC1 = 0
    carsC2 = 0
    carPreC1 = 0
    carPreC2 = 0

    carsB1 = 0
    carsB2 = 0
    carPreB1 = 0
    carPreB2 = 0

    carsD1 = 0
    carsD2 = 0
    carPreD1 = 0
    carPreD2 = 0

    interval = 90

    for car in cars:
        if car.goal == 1:
            if car.rect.centery <= 200:
                car.targetStart = 200
                car.targetStart = car.targetStart - carsA1 * interval
                carsA1 += 1
                carPreA1 = keepInterval(car, carsA1, carPreA1, interval)

        elif 2 <= car.goal <= 3:
            if car.rect.centery <= 200:
                car.targetStart = 200
                car.targetStart = car.targetStart - carsA2 * interval
                carsA2 += 1
                carPreA2 = keepInterval(car, carsA2, carPreA2, interval)

        elif car.goal == 4:
            if car.rect.centery >= 661:
                car.targetStart = 661
                car.targetStart = car.targetStart + carsC1 * interval
                carsC1 += 1
                carPreC1 = keepInterval(car, carsC1, carPreC1, interval)

        elif 5 <= car.goal <= 6:
            if car.rect.centery >= 661:
                car.targetStart = 661
                car.targetStart = car.targetStart + carsC2 * interval
                carsC2 += 1
                carPreC2 = keepInterval(car, carsC2, carPreC2, interval)

        elif car.goal == 7:
            if car.rect.centerx >= 661:
                if car.row != 90:
                    car.row = 90
                car.targetStart = 661
                car.targetStart = car.targetStart + carsB1 * interval
                carsB1 += 1
                carPreB1 = keepInterval(car, carsB1, carPreB1, interval)

        elif 8 <= car.goal <= 9:
            if car.rect.centerx >= 661:
                if car.row!=90:
                    car.row = 90
                car.targetStart = 661
                car.targetStart = car.targetStart + carsB2 * interval
                carsB2 += 1
                carPreB2 = keepInterval(car, carsB2, carPreB2, interval)

        elif car.goal == 10:
            if car.rect.centerx <= 200:
                if car.row != 90:
                    car.row = 90
                car.targetStart = 200
                car.targetStart = car.targetStart - carsD1 * interval
                carsD1 += 1
                carPreD1 = keepInterval(car, carsD1, carPreD1, interval)

        elif 11 <= car.goal <= 12:
            if car.rect.centerx <= 200:
                if car.row != 90:
                    car.row = 90
                car.targetStart = 200
                car.targetStart = car.targetStart - carsD2 * interval
                carsD2 += 1
                carPreD2 = keepInterval(car, carsD2, carPreD2, interval)


def keepInterval(car, carNo, carPre, interval):
    speed = 1
    if 1 <= car.goal <= 3:
        if car.rect.centery < car.targetStart:
            if carNo == 1:
                car.floaty += speed
                car.rect.centery = int(car.floaty)
            elif carPre - car.rect.centery >= interval:
                car.floaty += speed
                car.rect.centery = int(car.floaty)
        return car.rect.centery

    elif 4 <= car.goal <= 6:
        if car.rect.centery > car.targetStart:
            if carNo == 1:
                car.floaty -= speed
                car.rect.centery = int(car.floaty)
            elif car.rect.centery - carPre >= interval:
                car.floaty -= speed
                car.rect.centery = int(car.floaty)
        return car.rect.centery

    elif 7 <= car.goal <= 9:
        if car.rect.centerx > car.targetStart:
            if carNo == 1:
                car.floatx -= speed
                car.rect.centerx = int(car.floatx)
            elif car.rect.centerx - carPre >= interval:
                car.floatx -= speed
                car.rect.centerx = int(car.floatx)
        return car.rect.centerx

    elif 10 <= car.goal <= 12:
        if car.rect.centerx < car.targetStart:
            if carNo == 1:
                car.floatx += speed
                car.rect.centerx = int(car.floatx)
            elif carPre - car.rect.centerx >= interval:
                car.floatx += speed
                car.rect.centerx = int(car.floatx)
        return car.rect.centerx
