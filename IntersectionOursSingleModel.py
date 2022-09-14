import pygame
from Setting import Settings
from Intersection import Intersection
import Car_Function as cf
from build import Model
import time
# from time import *
import operation as op
import Car_Move as cm
import Car_position2marking as p2m
import Car_arrive as ca
import Car_Leave as cl
import pickle
import xlwt
import OptimalController as OC
import SimulationOperation as SO


class OurModel:
    def __init__(self):
        self.PIS = "0"
        self.fileNo = "0"

        # 创建一个屏幕对象
        pygame.init()
        self.ai_settings = Settings()  # 实例化
        self.screen = pygame.display.set_mode(
            (self.ai_settings.screen_width, self.ai_settings.screen_height)
        )
        pygame.display.set_caption("intersection mode")
        self.intersection = Intersection(self.screen)

    def mainMove(self, N):
        self.PIS = str(N)
        self.fileNo = str(N)

        muitMark = False
        leaveInter = 1
        PN = Model()
        fileNo = self.fileNo

        carsHis = []
        cars = []

        loopsFile = open('./data/' + fileNo + '/loopsfile.pkl', 'rb')
        loops = pickle.load(loopsFile)
        loopsFile.close()

        InsFile = open('./data/' + fileNo + '/Insfile.pkl', 'rb')
        Ins = pickle.load(InsFile)
        InsFile.close()
        # print(Ins)
        # print(loops)
        p = 0
        loop = 0

        TLeave = ['Ta17', 'Tb16', 'Tc18', 'Td15', 'Ta37', 'Tb36', 'Tc38', 'Td35', 'out']
        time.sleep(1)
        xs = []
        ys = []
        workbook = xlwt.Workbook(encoding='utf-8')
        worksheet = workbook.add_sheet('My Worksheet')
        worksheet.write(0, 0, "x")
        worksheet.write(0, 1, "y")

        waitTimes = []

        Mpre = op.CurM(PN)
        opt = []
        while loop <= 10000:
            # Goal = 1
            Mark = False
            if Mark:
                if loop < 1:
                    op.arriveRe(cars, self.screen, [12, 0, 0, 0], carsHis)
                for car in cars:
                    print(car.rect.centerx, car.rect.centery, car.row, car.goal)
            else:
                if p < len(loops) and loop == loops[p]:
                    In = Ins[p]
                    p = p + 1
                    op.arriveRe(cars, self.screen, In, carsHis)

            # 车辆达到>
            p2m.position2marking(PN, cars)
            carsInIntersection = []
            carsWait = []

            for car in cars:  # 先对车辆进行分类，区别交叉可内外车辆
                if car.curevent >= 1 and car.events[car.curevent] != "out":
                    carsInIntersection.append(car)
                elif car.curevent < 1:
                    carsWait.append(car)
                car.waitingTimeUpdate()

            if Mpre != op.CurM(PN):
                opt = OC.OptiamlSequence(carsInIntersection, PN)
                Mpre = op.CurM(PN)
            carsInIntersection = cf.leftTurnAdjust(carsInIntersection)
            # opt = ['T1l', 'T1a2',]# 'Ta2a4',  'T3l', 'T3b2', 'Tb2b4', 'Ta4b4','Tb4c4' ,'Tc38', 'out']
            # opt = ['T2l', 'T2c2','Tc2c4', 'Tc4d4', ]#'Td4a3',]

            # if len(opt)!=0:
            #     print(opt)
            #     # print(car.rect.centerx, car.rect.centery, car.row)

            # <实际move>
            ca.carArrive(cars)
            p2m.position2marking(PN, cars)
            OC.opt2ActionOptimal(carsInIntersection, opt, PN)

            carsLeave = []
            carsLeaveIntersection = 0
            for car in cars:
                if car.events[car.curevent] in TLeave and car not in carsLeave:  # 如果车辆已经离开路口 继续驶离
                    carsLeave.append(car)
                    carsLeaveIntersection += 1

            carsLeave = cl.orderCars(carsLeave)
            cl.carLeave(carsLeave)
            cm.cardel(cars, loop, muitMark, leaveInter)
            SO.drawLine(cars, self.screen)
            if len(cars) != 0:
                worksheet.write(loop + 1, 0, cars[0].rect.centerx)
                worksheet.write(loop + 1, 1, cars[0].rect.centery)
            else:
                workbook.save('./excel/targetLineGoal=' + '1' + '.xls')
            time.sleep(0.001)
            cf.update_screen(self.ai_settings, self.screen, self.intersection, cars)
            loop += 1

        return sum
