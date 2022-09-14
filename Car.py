import pygame
import pickle
import random

# import Car_Move


class Car:
    def __init__(self, screen, goal, curevent=0, leavemark=False, row=0):
        # 初始化car，并设置位置。
        self.screen = screen
        self.index = random.randint(1, 8)
        self.image = pygame.image.load('images/carS' + str(self.index) + '.png').convert_alpha()
        self.rect = self.image.get_rect()  # 实例
        self.screen_rect = screen.get_rect()  # 实例
        # 将car放在指定位置
        # self.rect.centerx = self.screen_rect.centerx
        # self.rect.bottom = self.screen_rect.bottom
        # self.rect = pygame.Rect(549, 240, 0, 0)
        self.row = row
        self.goal = goal  # 方向+意图 1=l,s,r
        self.curevent = curevent  # 当前车辆可发生事件
        self.leavemark = leavemark  # True 时 删除对象
        self.waitingTime = 0
        # if self.goal%3==2:
        #     self.image = pygame.image.load('images/carS.png')

        self.width = 28
        self.height = 47

        # file = open('./data/PathPoints/PathPointsGoal=' + str(goal) + '.pkl', 'rb')
        file = open('./data/PathPointsFinal/PathPointsFinalGoal=' + str(goal) + '.pkl', 'rb')
        self.PathPoints = pickle.load(file)
        file.close()
        # print(len(self.PathPoints))
        for i in range(0, len(self.PathPoints)):
            if int(self.PathPoints[i][1]) == 200 and 1 <= goal <= 3:
                self.Point = i
                # print(i)
                break
            if int(self.PathPoints[i][1]) == 661 and 4 <= goal <= 6:
                self.Point = i
                # print(i)
                break
            if int(self.PathPoints[i][0]) == 661 and 7 <= goal <= 9:
                self.Point = i
                # print(i)
                break
            if int(self.PathPoints[i][0]) == 200 and 10 <= goal <= 12:
                self.Point = i
                # print(i)
                break
        color = [(255, 150, 113), (242, 125, 136), (210, 111, 157), (163, 106, 170), (105, 103, 169), (27, 98, 153)]
        self.lineColor = color[random.randint(0, len(color) - 1)]

        if self.goal == 1:  # 1=l,s,r
            self.targetStart = 200
            self.rect = pygame.Rect(400, -80, self.width, self.height)  # l
            self.events = ['T1l', 'T1a2', 'TF1a2', 'Ta2a4', 'TFa2a4', 'Ta4b4', 'TFa4b4', 'Tb4c3', 'TFb4c3', 'Tc38',
                           'out']
        elif self.goal == 2:
            self.targetStart = 200
            self.rect = pygame.Rect(321, -80, self.width, self.height)  # s
            self.events = ['T1s', 'T1a1s', 'TF1a1s', 'Ta1a3', 'TFa1a3', 'Ta3d2', 'TFa3d2', 'Td2d1', 'TFd2d1', 'Td15',
                           'out']
            # self.image = pygame.image.load('images/carS1.png')
        elif self.goal == 3:
            self.targetStart = 200
            self.rect = pygame.Rect(323, -80, self.width, self.height)  # r
            self.events = ['T1r', 'T1a1r', 'TF1a1r', 'Ta17', 'out']

        elif self.goal == 4:  # 1=l,s,r
            self.targetStart = 661
            self.rect = pygame.Rect(477, 930, self.width, self.height)
            self.events = ['T2l', 'T2c2', 'TF2c2', 'Tc2c4', 'TFc2c4', 'Tc4d4', 'TFc4d4', 'Td4a3', 'TFd4a3', 'Ta37',
                           'out']
        elif self.goal == 5:
            self.targetStart = 661
            self.rect = pygame.Rect(555, 930, self.width, self.height)  # 初始位置
            self.events = ['T2s', 'T2c1s', 'TF2c1s', 'Tc1c3', 'TFc1c3', 'Tc3b2', 'TFc3b2', 'Tb2b1', 'TFb2b1', 'Tb16',
                           'out']
            # self.image = pygame.image.load('images/carS2.png')
        elif self.goal == 6:
            self.targetStart = 661
            self.rect = pygame.Rect(547, 930, self.width, self.height)  # 初始位置
            self.events = ['T2r', 'T2c1r', 'TF2c1r', 'Tc18', 'out']

        elif self.goal == 7:  # 1=l,s,r
            self.targetStart = 661
            self.rect = pygame.Rect(930, 404, self.width, self.height)
            self.events = ['T3l', 'T3b2', 'TF3b2', 'Tb2b4', 'TFb2b4', 'Tb4c4', 'TFb4c4', 'Tc4d3', 'TFc4d3', 'Td35',
                           'out']
        elif self.goal == 8:
            self.targetStart = 661
            self.rect = pygame.Rect(930, 321, self.width, self.height)  # 初始位置
            self.events = ['T3s', 'T3b1s', 'TF3b1s', 'Tb1b3', 'TFb1b3', 'Tb3a2', 'TFb3a2', 'Ta2a1', 'TFa2a1', 'Ta17',
                           'out']
            # self.image = pygame.image.load('images/carS3.png')
        elif self.goal == 9:
            self.targetStart = 661
            self.rect = pygame.Rect(930, 325, self.width, self.height)  # 初始位置
            self.events = ['T3r', 'T3b1r', 'TF3b1r', 'Tb16', 'out']

        elif self.goal == 10:  # 1=l,s,r
            self.targetStart = 200
            self.rect = pygame.Rect(-80, 479, self.width, self.height)
            self.events = ['T4l', 'T4d2', 'TF4d2', 'Td2d4', 'TFd2d4', 'Td4a4', 'TFd4a4', 'Ta4b3', 'TFa4b3', 'Tb36',
                           'out']
        elif self.goal == 11:
            self.targetStart = 200
            self.rect = pygame.Rect(-80, 545, self.width, self.height)  # 初始位置
            self.events = ['T4s', 'T4d1s', 'TF4d1s', 'Td1d3', 'TFd1d3', 'Td3c2', 'TFd3c2', 'Tc2c1', 'TFc2c1', 'Tc18',
                           'out']
            # self.image = pygame.image.load('images/carS4.png')
        elif self.goal == 12:
            self.targetStart = 200
            self.rect = pygame.Rect(-80, 549, self.width, self.height)  # 初始位置
            self.events = ['T4r', 'T4d1r', 'TF4d1r', 'Td15', 'out']

        self.floatx = float(self.rect.centerx)
        self.floaty = float(self.rect.centery)

        self.positionx = self.rect.centerx
        self.positiony = self.rect.centery
        self.init_positionx = self.rect.centerx
        self.init_positiony = self.rect.centery
        self.LINES_LIST = [(self.init_positionx, self.init_positiony), (self.init_positionx, self.init_positiony)]
        self.LINES_LIST_NEW = []
        self.path_point = []

    def blitme(self):
        # 在指定位置放置
        # self.image = pygame.image.load('images/carS' + str(self.index) + '.png').convert_alpha()
        curX = self.rect.centerx
        curY = self.rect.centery
        if self.goal == 11:
            self.rect.centery += 10
        try:
            self.image = pygame.transform.rotate(
                pygame.image.load('images/carS' + str(self.index) + '.png').convert_alpha(), self.row)
            self.screen.blit(self.image, self.rect)
        except:
            pass

        if self.goal == 11:
            self.rect.centery = curY

    def waitingTimeUpdate(self):
        if self.curevent == 1:
            self.waitingTime += 1

    # def rotate(self, deg):
    #     #if self.row!=deg:
    #         self.image = pygame.image.load('images/carS'+str(self.index)+'.png').convert_alpha()
    #         self.image = pygame.transform.rotate(self.image, deg)
    #         #self.row = deg
