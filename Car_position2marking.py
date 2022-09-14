import operation as op


def position2marking(PN, cars):
    Mref = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    op.writeM(Mref, PN)

    for car in cars:  # l s r
        car_x = car.rect.centerx
        car_y = car.rect.centery
        if car.goal == 1:
            if car_y < 200:
                PN.P1.token += 1
                car.curevent = 0
            elif car_y == 200:
                PN.Pw1a2.token = 1
                car.curevent = 1
            elif 345 >= car_y > 200:
                PN.P1a2.token = 1
                PN.Pa2.token = 0
                if car_y == 345:
                    PN.TF1a2.end = 0  # 事件完成
                    PN.P1a2.token = 0  # 进入下一个状态
                    PN.Pwa2a4.token = 1
                    car.curevent = 3

            elif 405 >= car_y > 345 and car_x <= 494:
                PN.Pa2a4.token = 1
                PN.Pa4.token = 0
                if car_y == 405:
                    PN.TFa2a4.end = 0
                    PN.Pa2a4.token = 0
                    PN.Pwa4b4.token = 1
                    car.curevent = 5

            elif 450 >= car_y > 405 and car_x <= 494:
                PN.Pa4b4.token = 1
                PN.Pb4.token = 0
                if car_y == 450:
                    PN.TFa4b4.end = 0
                    PN.Pa4b4.token = 0
                    PN.Pwb4c3.token = 1
                    car.curevent = 7

            elif 565 >= car_x > 494:
                PN.Pb4c3.token = 1
                PN.Pc3.token = 0
                if car_x == 565:
                    PN.TFb4c3.end = 0
                    PN.Pb4c3.token = 0
                    PN.Pwc38.token = 1
                    car.curevent = 9
            else:
                car.curevent = 10

        if car.goal == 2:  # 1as ads
            if car_y < 200:
                PN.P1.token += 1
                car.curevent = 0
            elif car_y == 200:
                PN.Pw1a1s.token = 1
                car.curevent = 1
            elif 350 >= car_y > 200:
                PN.P1a1s.token = 1
                PN.Pa1.token = 0
                if car_y == 350:
                    PN.TF1a1s.end = 0
                    PN.P1a1s.token = 0
                    PN.Pwa1a3.token = 1
                    car.curevent = 3

            elif 425 >= car_y > 350:
                PN.Pa1a3.token = 1
                PN.Pa3.token = 0
                if car_y == 425:
                    PN.TFa1a3.end = 0
                    PN.Pa1a3.token = 0
                    PN.Pwa3d2.token = 1
                    car.curevent = 5

            elif 500 >= car_y > 425:
                PN.Pa3d2.token = 1
                PN.Pd2.token = 0
                if car_y == 500:
                    PN.TFa3d2.end = 0
                    PN.Pa3d2.token = 0
                    PN.Pwd2d1.token = 1
                    car.curevent = 7

            elif 575 >= car_y > 500:
                PN.Pd2d1.token = 1
                PN.Pd1.token = 0
                if car_y == 575:
                    PN.TFd2d1.end = 0
                    PN.Pd2d1.token = 0
                    PN.Pwd15.token = 1
                    car.curevent = 9
            else:
                car.curevent = 10

        if car.goal == 3:  # 1ar
            if car_y < 200:
                PN.P1.token += 1
                car.curevent = 0
            elif car_y == 200:
                PN.Pw1a1r.token = 1
                car.curevent = 1
            elif 340 >= car_y > 200 and 337 >= car_x >= 280:
                PN.P1a1r.token = 1
                PN.Pa1.token = 0
                if car_y == 340:
                    if 337 >= car_x > 280:
                        PN.TF1a1r.end = 3
                    else:
                        PN.TF1a1r.end = 0
                        PN.P1a1r.token = 0
                        PN.Pwa17.token = 1
                        car.curevent = 3
            else:
                car.curevent = 4

        if car.goal == 4:  # 2cl
            if car_y > 661:
                PN.P2.token += 1
                car.curevent = 0
            elif car_y == 661:
                PN.Pw2c2.token = 1
                car.curevent = 1
            elif 557 <= car_y < 661:
                PN.P2c2.token = 1
                PN.Pc2.token = 0
                if car_y == 557:
                    PN.TF2c2.end = 0  # 事件完成
                    PN.P2c2.token = 0  # 进入下一个状态
                    PN.Pwc2c4.token = 1
                    car.curevent = 3

            elif 485 <= car_y < 557 and car_x >= 393:
                PN.Pc2c4.token = 1
                PN.Pc4.token = 0
                if car_y == 485:
                    PN.TFc2c4.end = 0
                    PN.Pc2c4.token = 0
                    PN.Pwc4d4.token = 1
                    car.curevent = 5

            elif 435 <= car_y < 485 and car_x >= 393:
                PN.Pc4d4.token = 1
                PN.Pd4.token = 0
                if car_y == 435:
                    PN.TFc4d4.end = 0
                    PN.Pc4d4.token = 0
                    PN.Pwd4a3.token = 1
                    car.curevent = 7

            elif 393 > car_x >= 322:
                PN.Pd4a3.token = 1
                PN.Pa3.token = 0
                if car_x == 322:
                    PN.TFd4a3.end = 0
                    PN.Pd4a3.token = 0
                    PN.Pwa37.token = 1
                    car.curevent = 9
            else:
                car.curevent = 10

        if car.goal == 5:  # 2cs cbs
            if car_y > 661:
                PN.P2.token += 1
                car.curevent = 0
            elif car_y == 661:
                PN.Pw2c1s.token = 1
                car.curevent = 1
            elif 558 <= car_y < 661:
                PN.P2c1s.token = 1
                PN.Pc1.token = 0
                if car_y == 558:
                    PN.TF2c1s.end = 0
                    PN.P2c1s.token = 0
                    PN.Pwc1c3.token = 1
                    car.curevent = 3

            elif 485 <= car_y < 558:
                PN.Pc1c3.token = 1
                PN.Pc3.token = 0
                if car_y == 485:
                    PN.TFc1c3.end = 0
                    PN.Pc1c3.token = 0
                    PN.Pwc3b2.token = 1
                    car.curevent = 5

            elif 410 <= car_y < 485:
                PN.Pc3b2.token = 1
                PN.Pb2.token = 0
                if car_y == 410:
                    PN.TFc3b2.end = 0
                    PN.Pc3b2.token = 0
                    PN.Pwb2b1.token = 1
                    car.curevent = 7

            elif 332 <= car_y < 410:
                PN.Pb2b1.token = 1
                PN.Pb1.token = 0
                if car_y == 332:
                    PN.TFb2b1.end = 0
                    PN.Pb2b1.token = 0
                    PN.Pwb16.token = 1
                    car.curevent = 9
            else:
                car.curevent = 10

        if car.goal == 6:  # 2cr
            if car_y > 661:
                PN.P2.token += 1
                car.curevent = 0
            elif car_y == 661:
                PN.Pw2c1r.token = 1
                car.curevent = 1
            elif 575 <= car_y < 661 and 610 >= car_x >= 560:
                PN.P2c1r.token = 1
                PN.Pc1.token = 0
                if car_y == 575:
                    if 610 > car_x >= 560:
                        PN.TF2c1r.end = 3
                    else:
                        PN.TF2c1r.end = 0
                        PN.P2c1r.token = 0
                        PN.Pwc18.token = 1
                        car.curevent = 3
            else:
                car.curevent = 4

        if car.goal == 7:  # 3bl
            if car_x > 661:
                PN.P3.token += 1
                car.curevent = 0
            elif car_x == 661:
                PN.Pw3b2.token = 1
                car.curevent = 1
            elif 548 <= car_x < 661:
                PN.P3b2.token = 1
                PN.Pb2.token = 0
                if car_x == 548:
                    PN.TF3b2.end = 0  # 事件完成
                    PN.P3b2.token = 0  # 进入下一个状态
                    PN.Pwb2b4.token = 1
                    car.curevent = 3

            elif 483 <= car_x < 548 and car_y <= 495:
                PN.Pb2b4.token = 1
                PN.Pb4.token = 0
                if car_x == 483:
                    PN.TFb2b4.end = 0
                    PN.Pb2b4.token = 0
                    PN.Pwb4c4.token = 1
                    car.curevent = 5

            elif 440 <= car_x < 483 and car_y <= 495:
                PN.Pb4c4.token = 1
                PN.Pc4.token = 0
                if car_x == 440:
                    PN.TFb4c4.end = 0
                    PN.Pb4c4.token = 0
                    PN.Pwc4d3.token = 1
                    car.curevent = 7

            elif 575 >= car_y > 495:
                PN.Pc4d3.token = 1
                PN.Pd3.token = 0
                if car_y == 575:
                    PN.TFc4d3.end = 0
                    PN.Pc4d3.token = 0
                    PN.Pwd35.token = 1
                    car.curevent = 9
            else:
                car.curevent = 10

        if car.goal == 8:  # 3bs bas
            if car_x > 661:
                PN.P3.token += 1
                car.curevent = 0
            elif car_x == 661:
                PN.Pw3b1s.token = 1
                car.curevent = 1
            elif 550 <= car_x < 661:
                PN.P3b1s.token = 1
                PN.Pb1.token = 0
                if car_x == 550:
                    PN.TF3b1s.end = 0
                    PN.P3b1s.token = 0
                    PN.Pwb1b3.token = 1
                    car.curevent = 3

            elif 472 <= car_x < 550:
                PN.Pb1b3.token = 1
                PN.Pb3.token = 0
                if car_x == 472:
                    PN.TFb1b3.end = 0
                    PN.Pb1b3.token = 0
                    PN.Pwb3a2.token = 1
                    car.curevent = 5

            elif 396 <= car_x < 472:
                PN.Pb3a2.token = 1
                PN.Pa2.token = 0
                if car_x == 396:
                    PN.TFb3a2.end = 0
                    PN.Pb3a2.token = 0
                    PN.Pwa2a1.token = 1
                    car.curevent = 7

            elif 322 <= car_x < 396:
                PN.Pa2a1.token = 1
                PN.Pa1.token = 0
                if car_x == 322:
                    PN.TFa2a1.end = 0
                    PN.Pa2a1.token = 0
                    PN.Pwa17.token = 1
                    car.curevent = 9
            else:
                car.curevent = 10

        if car.goal == 9:  # 3br
            if car_x > 661:
                PN.P3.token += 1
                car.curevent = 0
            elif car_x == 661:
                PN.Pw3b1r.token = 1
                car.curevent = 1
            elif 565 <= car_x < 661 and 348 >= car_y >= 280:
                PN.P3b1r.token = 1
                PN.Pb1.token = 0
                if car_x == 565:
                    if 348 >= car_y > 280:
                        PN.TF3b1r.end = 3
                    else:
                        PN.TF3b1r.end = 0
                        PN.P3b1r.token = 0
                        PN.Pwb16.token = 1
                        car.curevent = 3
            else:
                car.curevent = 4

        if car.goal == 10:
            if car_x < 200:
                PN.P4.token += 1
                car.curevent = 0
            elif car_x == 200:
                PN.Pw4d2.token = 1
                car.curevent = 1
            elif 338 >= car_x > 200:
                PN.P4d2.token = 1
                PN.Pd2.token = 0
                if car_x == 338:
                    PN.TF4d2.end = 0  # 事件完成
                    PN.P4d2.token = 0  # 进入下一个状态
                    PN.Pwd2d4.token = 1
                    car.curevent = 3

            elif 402 >= car_x > 338 and car_y >= 407:
                PN.Pd2d4.token = 1
                PN.Pd4.token = 0
                if car_x == 402:
                    PN.TFd2d4.end = 0
                    PN.Pd2d4.token = 0
                    PN.Pwd4a4.token = 1
                    car.curevent = 5

            elif 450 >= car_x > 402 and car_y >= 406:
                PN.Pd4a4.token = 1
                PN.Pa4.token = 0
                if car_x == 450:
                    PN.TFd4a4.end = 0
                    PN.Pd4a4.token = 0
                    PN.Pwa4b3.token = 1
                    car.curevent = 7

            elif 406 > car_y >= 332:
                PN.Pa4b3.token = 1
                PN.Pb3.token = 0
                if car_y == 332:
                    PN.TFa4b3.end = 0
                    PN.Pa4b3.token = 0
                    PN.Pwb36.token = 1
                    car.curevent = 9
            else:
                car.curevent = 10

        if car.goal == 11:  # 4ds dcs
            if car_x < 200:
                PN.P4.token += 1
                car.curevent = 0
            elif car_x == 200:
                PN.Pw4d1s.token = 1
                car.curevent = 1
            elif 340 >= car_x > 200:
                PN.P4d1s.token = 1
                PN.Pd1.token = 0
                if car_x == 340:
                    PN.TF4d1s.end = 0
                    PN.P4d1s.token = 0
                    PN.Pwd1d3.token = 1
                    car.curevent = 3

            elif 414 >= car_x > 340:
                PN.Pd1d3.token = 1
                PN.Pd3.token = 0
                if car_x == 414:
                    PN.TFd1d3.end = 0
                    PN.Pd1d3.token = 0
                    PN.Pwd3c2.token = 1
                    car.curevent = 5

            elif 488 >= car_x > 414:
                PN.Pd3c2.token = 1
                PN.Pc2.token = 0
                if car_x == 488:
                    PN.TFd3c2.end = 0
                    PN.Pd3c2.token = 0
                    PN.Pwc2c1.token = 1
                    car.curevent = 7

            elif 565 >= car_x > 488:
                PN.Pc2c1.token = 1
                PN.Pc1.token = 0
                if car_x == 565:
                    PN.TFc2c1.end = 0
                    PN.Pc2c1.token = 0
                    PN.Pwc18.token = 1
                    car.curevent = 9
            else:
                car.curevent = 10

        if car.goal == 12:  # 4dr
            if car_x < 200:
                PN.P4.token += 1
                car.curevent = 0
            elif car_x == 200:
                PN.Pw4d1r.token = 1
                car.curevent = 1
            elif 340 >= car_x > 200 and 600 >= car_y >= 545:
                PN.P4d1r.token = 1
                PN.Pd1.token = 0
                if car_x == 340:
                    if 600 > car_y >= 545:
                        PN.TF4d1r.end = 3
                    else:
                        PN.TF4d1r.end = 0
                        PN.P4d1r.token = 0
                        PN.Pwd15.token = 1
                        car.curevent = 3
            else:
                car.curevent = 4