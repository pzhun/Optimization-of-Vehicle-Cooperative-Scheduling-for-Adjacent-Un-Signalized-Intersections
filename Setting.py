import random
import pygame


class Settings():

    def __init__(self):
        #屏幕设置
        self.screen_width = 910
        self.screen_height = 910
        self.bg_color = (230,230,230)

def Poisson(N):
    m=random.randint(1,100)
    if N==0.25:
        if 1<=m<=80:
            cars=0
        elif 81<=m<=95:
            cars=1
        else:
            cars=2

    if N==0.5:
        if 1<=m<=55:
            cars=0
        elif 56<=m<=95:
            cars=1
        else:
            cars=2

    if N==1:
        if 1<=m<=20:
            cars=0
        elif 21<=m<=80:
            cars=1
        else:
            cars=2

    if N==0.75:
        if 1<=m<=30:
            cars=0
        elif 31<=m<=95:
            cars=1
        elif 96<=m<=100:
            cars=2

    if N==1.25:
        if 1<=m<=15:
            cars=0
        elif 15<=m<=70:
            cars=1
        elif 71<=m<=100:
            cars=2

    if N==1.1:
        if 1 <= m <= 15:
            cars = 0
        elif 16 <= m <= 75:
            cars = 1
        else:
            cars = 2

    if N==2:
        if 1<=m<=10:
            cars=0
        elif 11<=m<=30:
            cars=1
        elif 31<=m<=70:
            cars=2
        else:
            cars=3

    if N==0.1:
        if 1<=m<=10:
            cars=1
        else:
            cars=0

    if N==0.13:
        if 1<=m<=13:
            cars=1
        else:
            cars=0

    if N==0.2:
        if 1<=m<=20:
            cars=1
        else:
            cars=0


    if N==0.17:
        if 1<=m<=17:
            cars=1
        else:
            cars=0

    return cars