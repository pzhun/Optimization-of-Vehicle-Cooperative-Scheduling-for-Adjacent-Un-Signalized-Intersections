from place import Place, RoadPlace, TimedTransition, Transition


class Model:
    GreedMark = False
    Pa1 = RoadPlace('Pa1')
    Pa2 = RoadPlace('Pa2')
    Pa3 = RoadPlace('Pa3')
    Pa4 = RoadPlace('Pa4')

    Pb1 = RoadPlace('Pb1')
    Pb2 = RoadPlace('Pb2')
    Pb3 = RoadPlace('Pb3')
    Pb4 = RoadPlace('Pb4')

    Pc1 = RoadPlace('Pc1')
    Pc2 = RoadPlace('Pc2')
    Pc3 = RoadPlace('Pc3')
    Pc4 = RoadPlace('Pc4')

    Pd1 = RoadPlace('Pd1')
    Pd2 = RoadPlace('Pd2')
    Pd3 = RoadPlace('Pd3')
    Pd4 = RoadPlace('Pd4')  # 建立所有路权

    T1 = Transition('T1')
    T2 = Transition('T2')
    T3 = Transition('T3')
    T4 = Transition('T4')  # 车辆到达

    P1 = Place('P1')
    P2 = Place('P2')
    P3 = Place('P3')
    P4 = Place('P4')  # 等待车辆数

    T1r = Transition('T1r')
    T2r = Transition('T2r')
    T3r = Transition('T3r')
    T4r = Transition('T4r')  # 进入直行或右转车道

    T1s = Transition('T1s')
    T2s = Transition('T2s')
    T3s = Transition('T3s')
    T4s = Transition('T4s')  # 进入直行或右转车道

    T1l = Transition('T1l')
    T2l = Transition('T2l')
    T3l = Transition('T3l')
    T4l = Transition('T4l')  # 进入左转车道

    Pw1a1r = Place('Pw1a1r')
    Pw2c1r = Place('Pw2c1r')
    Pw3b1r = Place('Pw3b1r')
    Pw4d1r = Place('Pw4d1r')  # 等待直行或者转弯

    Pw1a1s = Place('Pw1a1s')
    Pw2c1s = Place('Pw2c1s')
    Pw3b1s = Place('Pw3b1s')
    Pw4d1s = Place('Pw4d1s')  # 等待直行或者转弯

    Pw1a2 = Place('Pw1a2')
    Pw2c2 = Place('Pw2c2')
    Pw3b2 = Place('Pw3b2')
    Pw4d2 = Place('Pw4d2')  # 等待左转

    T1a1r = Transition('T1a1r')
    T2c1r = Transition('T2c1r')
    T3b1r = Transition('T3b1r')
    T4d1r = Transition('T4d1r')  # 开始右转

    T1a1s = Transition('T1a1s')
    T2c1s = Transition('T2c1s')
    T3b1s = Transition('T3b1s')
    T4d1s = Transition('T4d1s')  # 开始直行

    T1a2 = Transition('T1a2')
    T2c2 = Transition('T2c2')
    T3b2 = Transition('T3b2')
    T4d2 = Transition('T4d2')  # 开始左转

    P1a1r = Place('P1a1r')
    P2c1r = Place('P2c1r')
    P3b1r = Place('P3b1r')
    P4d1r = Place('P4d1r')  # 转弯中

    P1a1s = Place('P1a1s')
    P2c1s = Place('P2c1s')
    P3b1s = Place('P3b1s')
    P4d1s = Place('P4d1s')  # 直行中

    P1a2 = Place('P1a2')
    P2c2 = Place('P2c2')
    P3b2 = Place('P3b2')
    P4d2 = Place('P4d2')  # 左转中

    TF1a2 = TimedTransition('TF1a2', 3)
    TF2c2 = TimedTransition('TF2c2', 3)
    TF3b2 = TimedTransition('TF3b2', 3)
    TF4d2 = TimedTransition('TF4d2', 3)  # 左转完成

    TF1a1s = TimedTransition('TF1a1s', 2)
    TF2c1s = TimedTransition('TF2c1s', 2)
    TF3b1s = TimedTransition('TF3b1s', 2)
    TF4d1s = TimedTransition('TF4d1s', 2)  # 直行完成

    TF1a1r = TimedTransition('TF1a1r', 4)
    TF2c1r = TimedTransition('TF2c1r', 4)
    TF3b1r = TimedTransition('TF3b1r', 4)
    TF4d1r = TimedTransition('TF4d1r', 4)  # 右转完成

    Pwa17 = Place('Pwa17')
    Pwb16 = Place('Pwb16')
    Pwc18 = Place('Pwc18')
    Pwd15 = Place('Pwd15')  # 等待驶离

    Pwa1a3 = Place('Pwa1a3')
    Pwb1b3 = Place('Pwb1b3')
    Pwc1c3 = Place('Pwc1c3')
    Pwd1d3 = Place('Pwd1d3')  # 等待继续直行

    Pwa2a4 = Place('Pwa2a4')
    Pwb2b4 = Place('Pwb2b4')
    Pwc2c4 = Place('Pwc2c4')
    Pwd2d4 = Place('Pwd2d4')  # 等待是否可以进入e

    Ta17 = Transition('Ta17')
    Tb16 = Transition('Tb16')
    Tc18 = Transition('Tc18')
    Td15 = Transition('Td15')  # 驶离

    Ta1a3 = Transition('Ta1a3')
    Tb1b3 = Transition('Tb1b3')
    Tc1c3 = Transition('Tc1c3')
    Td1d3 = Transition('Td1d3')  # 开始继续直行

    Pa1a3 = Place('Pa1a3')
    Pb1b3 = Place('Pb1b3')
    Pc1c3 = Place('Pc1c3')
    Pd1d3 = Place('Pd1d3')  # 继续直行中

    TFa1a3 = TimedTransition('TFa1a3', 2)
    TFb1b3 = TimedTransition('TFb1b3', 2)
    TFc1c3 = TimedTransition('TFc1c3', 2)
    TFd1d3 = TimedTransition('TFd1d3', 2)  # 完成继续直行

    Pwa3d2 = Place('Pwa3d2')
    Pwb3a2 = Place('Pwb3a2')
    Pwc3b2 = Place('Pwc3b2')
    Pwd3c2 = Place('Pwd3c2')  # 等待继续直行

    Ta3d2 = Transition('Ta3d2')
    Tb3a2 = Transition('Tb3a2')
    Tc3b2 = Transition('Tc3b2')
    Td3c2 = Transition('Td3c2')  # 继续直行

    Pa3d2 = Place('Pa3d2')
    Pb3a2 = Place('Pb3a2')
    Pc3b2 = Place('Pc3b2')
    Pd3c2 = Place('Pd3c2')  # 继续直行中

    TFa3d2 = TimedTransition('TFa3d2', 2)
    TFb3a2 = TimedTransition('TFb3a2', 2)
    TFc3b2 = TimedTransition('TFc3b2', 2)
    TFd3c2 = TimedTransition('TFd3c2', 2)  # 完成继续直行

    Pwd2d1 = Place('Pwd2d1')
    Pwa2a1 = Place('Pwa2a1')
    Pwc2c1 = Place('Pwc2c1')
    Pwb2b1 = Place('Pwb2b1')  # 等待继续直行

    Td2d1 = Transition('Td2d1')
    Ta2a1 = Transition('Ta2a1')
    Tb2b1 = Transition('Tb2b1')
    Tc2c1 = Transition('Tc2c1')  # 继续直行

    Pd2d1 = Place('Pd2d1')
    Pa2a1 = Place('Pa2a1')
    Pc2c1 = Place('Pc2c1')
    Pb2b1 = Place('Pb2b1')  # 等待继续直行

    TFd2d1 = TimedTransition('TFd2d1', 2)
    TFa2a1 = TimedTransition('TFa2a1', 2)
    TFb2b1 = TimedTransition('TFb2b1', 2)
    TFc2c1 = TimedTransition('TFc2c1', 2)  # 完成继续直行

    Ta2a4 = Transition('Ta2a4')
    Tb2b4 = Transition('Tb2b4')
    Tc2c4 = Transition('Tc2c4')
    Td2d4 = Transition('Td2d4')

    Pa2a4 = Place('Pa2a4')
    Pb2b4 = Place('Pb2b4')
    Pc2c4 = Place('Pc2c4')
    Pd2d4 = Place('Pd2d4')

    TFa2a4 = TimedTransition('TFa2a4', 2)
    TFb2b4 = TimedTransition('TFb2b4', 2)
    TFc2c4 = TimedTransition('TFc2c4', 2)
    TFd2d4 = TimedTransition('TFd2d4', 2)

    Pwa4b4 = Place('Pwa4b4')
    Pwb4c4 = Place('Pwb4c4')
    Pwc4d4 = Place('Pwc4d4')
    Pwd4a4 = Place('Pwd4a4')

    Ta4b4 = Transition('Ta4b4')  # 4
    Tb4c4 = Transition('Tb4c4')
    Tc4d4 = Transition('Tc4d4')
    Td4a4 = Transition('Td4a4')

    Pa4b4 = Place('Pa4b4')
    Pb4c4 = Place('Pb4c4')
    Pc4d4 = Place('Pc4d4')
    Pd4a4 = Place('Pd4a4')

    TFa4b4 = TimedTransition('TFa4b4', 2)
    TFb4c4 = TimedTransition('TFb4c4', 2)
    TFc4d4 = TimedTransition('TFc4d4', 2)
    TFd4a4 = TimedTransition('TFd4a4', 2)

    Pwa4b3 = Place('Pwa4b3')
    Pwb4c3 = Place('Pwb4c3')
    Pwc4d3 = Place('Pwc4d3')  # 等待继续左转
    Pwd4a3 = Place('Pwd4a3')

    Ta4b3 = Transition('Ta4b3')
    Tb4c3 = Transition('Tb4c3')
    Tc4d3 = Transition('Tc4d3')  # 继续左转
    Td4a3 = Transition('Td4a3')

    Pa4b3 = Place('Pa4b3')
    Pb4c3 = Place('Pb4c3')
    Pc4d3 = Place('Pc4d3')  # 继续左转中
    Pd4a3 = Place('Pd4a3')

    TFa4b3 = TimedTransition('TFa4b3', 2)
    TFb4c3 = TimedTransition('TFb4c3', 2)
    TFc4d3 = TimedTransition('TFc4d3', 2)  # 完成继续左转
    TFd4a3 = TimedTransition('TFd4a3', 2)

    Pwa37 = Place('Pwa37')
    Pwb36 = Place('Pwb36')
    Pwc38 = Place('Pwc38')
    Pwd35 = Place('Pwd35')  # 等待驶离

    Ta37 = Transition('Ta37')
    Tb36 = Transition('Tb36')
    Tc38 = Transition('Tc38')
    Td35 = Transition('Td35')  # 驶离

    RNode = [Pa1, Pa2, Pa3, Pb1, Pb2, Pb3, Pc1, Pc2, Pc3, Pd1, Pd2, Pd3]

    PNodes = [Pa1, Pa2, Pa3, Pa4, Pb1, Pb2, Pb3, Pb4, Pc1, Pc2, Pc3, Pc4, Pd1, Pd2, Pd3, Pd4,
              P1, P2, P3, P4,
              Pw1a1s, Pw2c1s, Pw3b1s, Pw4d1s, Pw1a1r, Pw2c1r, Pw3b1r, Pw4d1r, Pw1a2, Pw2c2, Pw3b2, Pw4d2,
              P1a1s, P2c1s, P3b1s, P4d1s, P1a1r, P2c1r, P3b1r, P4d1r, P1a2, P2c2, P3b2, P4d2,
              Pwa17, Pwb16, Pwc18, Pwd15,
              Pwa1a3, Pwb1b3, Pwc1c3, Pwd1d3, Pwa2a4, Pwb2b4, Pwc2c4, Pwd2d4,
              Pa1a3, Pb1b3, Pc1c3, Pd1d3, Pa2a4, Pb2b4, Pc2c4, Pd2d4,
              Pwa3d2, Pwb3a2, Pwc3b2, Pwd3c2, Pa3d2, Pb3a2, Pc3b2, Pd3c2,
              Pwd4a3, Pwa4b3, Pwb4c3, Pwc4d3, Pd4a3, Pa4b3, Pb4c3, Pc4d3,
              Pwd2d1, Pwa2a1, Pwc2c1, Pwb2b1, Pd2d1, Pa2a1, Pc2c1, Pb2b1,
              Pwa4b4, Pwb4c4, Pwc4d4, Pwd4a4, Pa4b4, Pb4c4, Pc4d4, Pd4a4,
              Pwa37, Pwb36, Pwc38, Pwd35
              ]  # 所有库所
    TNodes = [TF1a1r, TF2c1r, TF3b1r, TF4d1r, TF1a1s, TF2c1s, TF3b1s, TF4d1s, TF1a2, TF2c2, TF3b2, TF4d2,
              TFa1a3, TFb1b3, TFc1c3, TFd1d3,
              TFa3d2, TFb3a2, TFc3b2, TFd3c2,
              TFd2d1, TFa2a1, TFc2c1, TFb2b1,
              TFa2a4, TFb2b4, TFc2c4, TFd2d4,
              TFa4b4, TFb4c4, TFc4d4, TFd4a4,
              TFd4a3, TFa4b3, TFb4c3, TFc4d3,
              ]  # 时间变迁

    CNodes = [T1l, T2l, T3l, T4l, T1r, T2r, T3r, T4r, T1s, T2s, T3s, T4s,
              T1a1r, T2c1r, T3b1r, T4d1r, T1a1s, T2c1s, T3b1s, T4d1s, T1a2, T2c2, T3b2, T4d2,
              Ta1a3, Tb1b3, Tc1c3, Td1d3,
              Ta3d2, Tb3a2, Tc3b2, Td3c2,
              Td2d1, Ta2a1, Tc2c1, Tb2b1,
              Ta2a4, Tb2b4, Tc2c4, Td2d4,
              Ta4b4, Tb4c4, Tc4d4, Td4a4,
              Td4a3, Ta4b3, Tb4c3, Tc4d3,
              Ta17, Tb16, Tc18, Td15, Ta37, Tb36, Tc38, Td35,
              ]  # 瞬时变迁

    Nodes = [TF1a1r, TF2c1r, TF3b1r, TF4d1r, TF1a1s, TF2c1s, TF3b1s, TF4d1s, TF1a2, TF2c2, TF3b2, TF4d2,
             TFa1a3, TFb1b3, TFc1c3, TFd1d3,
             TFa3d2, TFb3a2, TFc3b2, TFd3c2,
             TFd2d1, TFa2a1, TFc2c1, TFb2b1,
             TFa2a4, TFb2b4, TFc2c4, TFd2d4,
             TFa4b4, TFb4c4, TFc4d4, TFd4a4,
             TFd4a3, TFa4b3, TFb4c3, TFc4d3,
             T1a1r, T2c1r, T3b1r, T4d1r, T1a1s, T2c1s, T3b1s, T4d1s, T1a2, T2c2, T3b2, T4d2,
             Ta1a3, Tb1b3, Tc1c3, Td1d3,
             Ta3d2, Tb3a2, Tc3b2, Td3c2,
             Td2d1, Ta2a1, Tc2c1, Tb2b1,
             Ta2a4, Tb2b4, Tc2c4, Td2d4,
             Ta4b4, Tb4c4, Tc4d4, Td4a4,
             Td4a3, Ta4b3, Tb4c3, Tc4d3,
             Ta17, Tb16, Tc18, Td15, Ta37, Tb36, Tc38, Td35
             ]  # 所有十字路口内的变迁

    ANodes = [T1l, T2l, T3l, T4l, T1r, T2r, T3r, T4r, T1s, T2s, T3s, T4s]
    PANodes = [P1, P2, P3, P4]
    PPNodes = [Pwa1a3, Pwb1b3, Pwc1c3, Pwd1d3, Pwa2a4, Pwb2b4, Pwc2c4, Pwd2d4,
               Pwa3d2, Pwb3a2, Pwc3b2, Pwd3c2,
               Pwd4a3, Pwa4b3, Pwb4c3, Pwc4d3,
               Pwd2d1, Pwa2a1, Pwc2c1, Pwb2b1,
               Pwa4b4, Pwb4c4, Pwc4d4, Pwd4a4, ]

    Tleave = [Ta17, Tb16, Tc18, Td15, Ta37, Tb36, Tc38, Td35]

    _1l = [T1l, T1a2, TF1a2, Ta2a4, TFa2a4, Ta4b4, TFa4b4, Tb4c3, TFb4c3, Tc38]
    _1s = [T1s, T1a1s, TF1a1s, Ta1a3, TFa1a3, Ta3d2, TFa3d2, Td2d1, TFd2d1, Td15]
    _1r = [T1r, T1a1r, TF1a1r, Ta17]

    _2l = [T2l, T2c2, TF2c2, Tc2c4, TFc2c4, Tc4d4, TFc4d4, Td4a3, TFd4a3, Ta37]
    _2s = [T2s, T2c1s, TF2c1s, Tc1c3, TFc1c3, Tc3b2, TFc3b2, Tb2b1, TFb2b1, Tb16]
    _2r = [T2r, T2c1r, TF2c1r, Tc18]

    _3l = [T3l, T3b2, TF3b2, Tb2b4, TFb2b4, Tb4c4, TFb4c4, Tc4d3, TFc4d3, Td35]
    _3s = [T3s, T3b1s, TF3b1s, Tb1b3, TFb1b3, Tb3a2, TFb3a2, Ta2a1, TFa2a1, Ta17]
    _3r = [T3r, T3b1r, TF3b1r, Tb16]

    _4l = [T4l, T4d2, TF4d2, Td2d4, TFd2d4, Td4a4, TFd4a4, Ta4b3, TFa4b3, Tb36]  #
    _4s = [T4s, T4d1s, TF4d1s, Td1d3, TFd1d3, Td3c2, TFd3c2, Tc2c1, TFc2c1, Tc18]
    _4r = [T4r, T4d1r, TF4d1r, Td15]

    _1l8 = [P1a2, Pa2a4, Pwa2a4, Pa4b4, Pwa4b4, Pb4c3, Pwb4c3, Pwc38]  # 内部，不算交叉口外的
    _1s5 = [P1a1s, Pa1a3, Pwa1a3, Pa3d2, Pwa3d2, Pd2d1, Pwd2d1, Pwd15]
    _1r7 = [P1a1r, Pwa17]

    _2l7 = [P2c2, Pc2c4, Pwc2c4, Pc4d4, Pwc4d4, Pd4a3, Pwd4a3, Pwa37]
    _2s6 = [P2c1s, Pc1c3, Pwc1c3, Pc3b2, Pwc3b2, Pb2b1, Pwb2b1, Pwb16]
    _2r8 = [P2c1r, Pwc18]

    _3l5 = [P3b2, Pb2b4, Pwb2b4, Pb4c4, Pwb4c4, Pc4d3, Pwc4d3, Pwd35]
    _3s7 = [P3b1s, Pb1b3, Pwb1b3, Pb3a2, Pwb3a2, Pa2a1, Pwa2a1, Pwa17]
    _3r6 = [P3b1r, Pwb16]

    _4l6 = [P4d2, Pd2d4, Pwd2d4, Pd4a4, Pwd4a4, Pa4b3, Pwa4b3, Pwb36]  #
    _4s8 = [P4d1s, Pd1d3, Pwd1d3, Pd3c2, Pwd3c2, Pc2c1, Pwc2c1, Pwc18]
    _4r5 = [P4d1r, Pwd15]

    Go5 = _1s5 + _4r5
    Go6 = _2s6 + _3r6
    Go7 = _1r7 + _3s7
    Go8 = _2r8 + _4s8

    Go5l = _3l5
    Go6l = _4l6
    Go7l = _2l7
    Go8l = _1l8

    Fulltransition = [_1l, _1s, _1r, _2l, _2s, _2r, _3l, _3s, _3r, _4l, _4s, _4r]

    # 添加arc
    T1.next.append(P1)
    T2.next.append(P2)
    T3.next.append(P3)
    T4.next.append(P4)

    P1.next.append(T1l)  # l s r
    P2.next.append(T2l)
    P3.next.append(T3l)
    P4.next.append(T4l)
    P1.next.append(T1s)
    P2.next.append(T2s)
    P3.next.append(T3s)
    P4.next.append(T4s)
    P1.next.append(T1r)
    P2.next.append(T2r)
    P3.next.append(T3r)
    P4.next.append(T4r)

    T1s.pre.append(P1)
    T2s.pre.append(P2)
    T3s.pre.append(P3)
    T4s.pre.append(P4)
    T1s.next.append(Pw1a1s)
    T2s.next.append(Pw2c1s)
    T3s.next.append(Pw3b1s)
    T4s.next.append(Pw4d1s)

    T1r.pre.append(P1)
    T2r.pre.append(P2)
    T3r.pre.append(P3)
    T4r.pre.append(P4)
    T1r.next.append(Pw1a1r)
    T2r.next.append(Pw2c1r)
    T3r.next.append(Pw3b1r)
    T4r.next.append(Pw4d1r)

    T1l.pre.append(P1)
    T2l.pre.append(P2)
    T3l.pre.append(P3)
    T4l.pre.append(P4)
    T1l.next.append(Pw1a2)
    T2l.next.append(Pw2c2)
    T3l.next.append(Pw3b2)
    T4l.next.append(Pw4d2)

    Pw1a1r.next.append(T1a1r)
    Pw2c1r.next.append(T2c1r)
    Pw3b1r.next.append(T3b1r)
    Pw4d1r.next.append(T4d1r)

    Pw1a1s.next.append(T1a1s)
    Pw2c1s.next.append(T2c1s)
    Pw3b1s.next.append(T3b1s)
    Pw4d1s.next.append(T4d1s)

    Pw1a2.next.append(T1a2)
    Pw2c2.next.append(T2c2)
    Pw3b2.next.append(T3b2)
    Pw4d2.next.append(T4d2)

    T1a1s.pre.append(Pw1a1s)
    T2c1s.pre.append(Pw2c1s)
    T3b1s.pre.append(Pw3b1s)
    T4d1s.pre.append(Pw4d1s)
    T1a1s.pre.append(Pa1)
    T2c1s.pre.append(Pc1)
    T3b1s.pre.append(Pb1)
    T4d1s.pre.append(Pd1)
    T1a1s.next.append(P1a1s)
    T2c1s.next.append(P2c1s)
    T3b1s.next.append(P3b1s)
    T4d1s.next.append(P4d1s)

    T1a1r.pre.append(Pw1a1r)
    T2c1r.pre.append(Pw2c1r)
    T3b1r.pre.append(Pw3b1r)
    T4d1r.pre.append(Pw4d1r)
    T1a1r.pre.append(Pa1)
    T2c1r.pre.append(Pc1)
    T3b1r.pre.append(Pb1)
    T4d1r.pre.append(Pd1)
    T1a1r.next.append(P1a1r)
    T2c1r.next.append(P2c1r)
    T3b1r.next.append(P3b1r)
    T4d1r.next.append(P4d1r)

    T1a2.pre.append(Pw1a2)
    T2c2.pre.append(Pw2c2)
    T3b2.pre.append(Pw3b2)
    T4d2.pre.append(Pw4d2)
    T1a2.pre.append(Pa2)
    T2c2.pre.append(Pc2)
    T3b2.pre.append(Pb2)
    T4d2.pre.append(Pd2)
    T1a2.next.append(P1a2)
    T2c2.next.append(P2c2)
    T3b2.next.append(P3b2)
    T4d2.next.append(P4d2)

    P1a1r.next.append(TF1a1r)
    P2c1r.next.append(TF2c1r)
    P3b1r.next.append(TF3b1r)
    P4d1r.next.append(TF4d1r)

    P1a1s.next.append(TF1a1s)
    P2c1s.next.append(TF2c1s)
    P3b1s.next.append(TF3b1s)
    P4d1s.next.append(TF4d1s)

    P1a2.next.append(TF1a2)
    P2c2.next.append(TF2c2)
    P3b2.next.append(TF3b2)
    P4d2.next.append(TF4d2)

    TF1a1r.pre.append(P1a1r)
    TF2c1r.pre.append(P2c1r)
    TF3b1r.pre.append(P3b1r)
    TF4d1r.pre.append(P4d1r)
    TF1a1r.next.append(Pwa17)
    TF2c1r.next.append(Pwc18)
    TF3b1r.next.append(Pwb16)
    TF4d1r.next.append(Pwd15)

    TF1a1s.pre.append(P1a1s)
    TF2c1s.pre.append(P2c1s)
    TF3b1s.pre.append(P3b1s)
    TF4d1s.pre.append(P4d1s)
    TF1a1s.next.append(Pwa1a3)
    TF2c1s.next.append(Pwc1c3)
    TF3b1s.next.append(Pwb1b3)
    TF4d1s.next.append(Pwd1d3)

    TF1a2.pre.append(P1a2)
    TF2c2.pre.append(P2c2)
    TF3b2.pre.append(P3b2)
    TF4d2.pre.append(P4d2)
    TF1a2.next.append(Pwa2a4)
    TF2c2.next.append(Pwc2c4)
    TF3b2.next.append(Pwb2b4)
    TF4d2.next.append(Pwd2d4)

    Pwa17.next.append(Ta17)
    Pwb16.next.append(Tb16)
    Pwc18.next.append(Tc18)
    Pwd15.next.append(Td15)

    Pwa1a3.next.append(Ta1a3)
    Pwb1b3.next.append(Tb1b3)
    Pwc1c3.next.append(Tc1c3)
    Pwd1d3.next.append(Td1d3)

    Pwa2a4.next.append(Ta2a4)
    Pwb2b4.next.append(Tb2b4)
    Pwc2c4.next.append(Tc2c4)
    Pwd2d4.next.append(Td2d4)

    Ta17.pre.append(Pwa17)
    Tb16.pre.append(Pwb16)
    Tc18.pre.append(Pwc18)
    Td15.pre.append(Pwd15)
    Ta17.next.append(Pa1)
    Tb16.next.append(Pb1)
    Tc18.next.append(Pc1)
    Td15.next.append(Pd1)

    Ta1a3.pre.append(Pwa1a3)
    Tb1b3.pre.append(Pwb1b3)
    Tc1c3.pre.append(Pwc1c3)
    Td1d3.pre.append(Pwd1d3)
    Ta1a3.pre.append(Pa3)
    Tb1b3.pre.append(Pb3)
    Tc1c3.pre.append(Pc3)
    Td1d3.pre.append(Pd3)
    Ta1a3.next.append(Pa1a3)
    Tb1b3.next.append(Pb1b3)
    Tc1c3.next.append(Pc1c3)
    Td1d3.next.append(Pd1d3)
    Ta1a3.next.append(Pa1)
    Tb1b3.next.append(Pb1)
    Tc1c3.next.append(Pc1)
    Td1d3.next.append(Pd1)

    Ta2a4.pre.append(Pwa2a4)
    Tb2b4.pre.append(Pwb2b4)
    Tc2c4.pre.append(Pwc2c4)
    Td2d4.pre.append(Pwd2d4)
    Ta2a4.pre.append(Pa4)
    Tb2b4.pre.append(Pb4)
    Tc2c4.pre.append(Pc4)
    Td2d4.pre.append(Pd4)
    Ta2a4.next.append(Pa2a4)
    Tb2b4.next.append(Pb2b4)
    Tc2c4.next.append(Pc2c4)
    Td2d4.next.append(Pd2d4)
    Ta2a4.next.append(Pa2)
    Tb2b4.next.append(Pb2)
    Tc2c4.next.append(Pc2)
    Td2d4.next.append(Pd2)

    Pa1a3.next.append(TFa1a3)
    Pb1b3.next.append(TFb1b3)
    Pc1c3.next.append(TFc1c3)
    Pd1d3.next.append(TFd1d3)

    Pa2a4.next.append(TFa2a4)
    Pb2b4.next.append(TFb2b4)
    Pc2c4.next.append(TFc2c4)
    Pd2d4.next.append(TFd2d4)

    TFa1a3.pre.append(Pa1a3)
    TFb1b3.pre.append(Pb1b3)
    TFc1c3.pre.append(Pc1c3)
    TFd1d3.pre.append(Pd1d3)
    TFa1a3.next.append(Pwa3d2)
    TFb1b3.next.append(Pwb3a2)
    TFc1c3.next.append(Pwc3b2)
    TFd1d3.next.append(Pwd3c2)

    TFa2a4.pre.append(Pa2a4)
    TFb2b4.pre.append(Pb2b4)
    TFc2c4.pre.append(Pc2c4)
    TFd2d4.pre.append(Pd2d4)
    TFa2a4.next.append(Pwa4b4)
    TFb2b4.next.append(Pwb4c4)
    TFc2c4.next.append(Pwc4d4)
    TFd2d4.next.append(Pwd4a4)

    Pwa3d2.next.append(Ta3d2)
    Pwb3a2.next.append(Tb3a2)
    Pwc3b2.next.append(Tc3b2)
    Pwd3c2.next.append(Td3c2)

    Pwa4b4.next.append(Ta4b4)
    Pwb4c4.next.append(Tb4c4)
    Pwc4d4.next.append(Tc4d4)
    Pwd4a4.next.append(Td4a4)

    Ta3d2.pre.append(Pwa3d2)
    Tb3a2.pre.append(Pwb3a2)
    Tc3b2.pre.append(Pwc3b2)
    Td3c2.pre.append(Pwd3c2)
    Ta3d2.pre.append(Pd2)
    Tb3a2.pre.append(Pa2)
    Tc3b2.pre.append(Pb2)
    Td3c2.pre.append(Pc2)
    Ta3d2.next.append(Pa3d2)
    Tb3a2.next.append(Pb3a2)
    Tc3b2.next.append(Pc3b2)
    Td3c2.next.append(Pd3c2)
    Ta3d2.next.append(Pa3)
    Tb3a2.next.append(Pb3)
    Tc3b2.next.append(Pc3)
    Td3c2.next.append(Pd3)

    Ta4b4.pre.append(Pwa4b4)
    Tb4c4.pre.append(Pwb4c4)
    Tc4d4.pre.append(Pwc4d4)
    Td4a4.pre.append(Pwd4a4)
    Ta4b4.pre.append(Pb4)
    Tb4c4.pre.append(Pc4)
    Tc4d4.pre.append(Pd4)
    Td4a4.pre.append(Pa4)
    Ta4b4.next.append(Pa4b4)
    Tb4c4.next.append(Pb4c4)
    Tc4d4.next.append(Pc4d4)
    Td4a4.next.append(Pd4a4)

    Pa3d2.next.append(TFa3d2)
    Pb3a2.next.append(TFb3a2)
    Pc3b2.next.append(TFc3b2)
    Pd3c2.next.append(TFd3c2)

    Pa4b4.next.append(TFa4b4)
    Pb4c4.next.append(TFb4c4)
    Pc4d4.next.append(TFc4d4)
    Pd4a4.next.append(TFd4a4)

    TFa3d2.pre.append(Pa3d2)
    TFb3a2.pre.append(Pb3a2)
    TFc3b2.pre.append(Pc3b2)
    TFd3c2.pre.append(Pd3c2)
    TFa3d2.next.append(Pwd2d1)
    TFb3a2.next.append(Pwa2a1)
    TFc3b2.next.append(Pwb2b1)
    TFd3c2.next.append(Pwc2c1)

    TFa4b4.pre.append(Pa4b4)
    TFb4c4.pre.append(Pb4c4)
    TFc4d4.pre.append(Pc4d4)
    TFd4a4.pre.append(Pd4a4)
    TFa4b4.next.append(Pwb4c3)
    TFb4c4.next.append(Pwc4d3)
    TFc4d4.next.append(Pwd4a3)
    TFd4a4.next.append(Pwa4b3)

    Pwd2d1.next.append(Td2d1)
    Pwa2a1.next.append(Ta2a1)
    Pwc2c1.next.append(Tc2c1)
    Pwb2b1.next.append(Tb2b1)

    Pwd4a3.next.append(Td4a3)
    Pwa4b3.next.append(Ta4b3)
    Pwb4c3.next.append(Tb4c3)
    Pwc4d3.next.append(Tc4d3)

    Td2d1.pre.append(Pwd2d1)
    Ta2a1.pre.append(Pwa2a1)
    Tb2b1.pre.append(Pwb2b1)
    Tc2c1.pre.append(Pwc2c1)
    Td2d1.pre.append(Pd1)
    Ta2a1.pre.append(Pa1)
    Tb2b1.pre.append(Pb1)
    Tc2c1.pre.append(Pc1)
    Td2d1.next.append(Pd2d1)
    Ta2a1.next.append(Pa2a1)
    Tb2b1.next.append(Pb2b1)
    Tc2c1.next.append(Pc2c1)
    Td2d1.next.append(Pd2)
    Ta2a1.next.append(Pa2)
    Tb2b1.next.append(Pb2)
    Tc2c1.next.append(Pc2)

    Td4a3.pre.append(Pwd4a3)
    Ta4b3.pre.append(Pwa4b3)
    Tb4c3.pre.append(Pwb4c3)
    Tc4d3.pre.append(Pwc4d3)
    Td4a3.pre.append(Pa3)
    Ta4b3.pre.append(Pb3)
    Tb4c3.pre.append(Pc3)
    Tc4d3.pre.append(Pd3)
    Td4a3.next.append(Pd4a3)
    Ta4b3.next.append(Pa4b3)
    Tb4c3.next.append(Pb4c3)
    Tc4d3.next.append(Pc4d3)
    Td4a3.next.append(Pd4)
    Ta4b3.next.append(Pa4)
    Tb4c3.next.append(Pb4)
    Tc4d3.next.append(Pc4)

    Pd2d1.next.append(TFd2d1)
    Pa2a1.next.append(TFa2a1)
    Pb2b1.next.append(TFb2b1)
    Pc2c1.next.append(TFc2c1)

    Pd4a3.next.append(TFd4a3)
    Pa4b3.next.append(TFa4b3)
    Pb4c3.next.append(TFb4c3)
    Pc4d3.next.append(TFc4d3)

    TFd2d1.pre.append(Pd2d1)
    TFa2a1.pre.append(Pa2a1)
    TFb2b1.pre.append(Pb2b1)
    TFc2c1.pre.append(Pc2c1)
    TFd2d1.next.append(Pwd15)
    TFa2a1.next.append(Pwa17)
    TFb2b1.next.append(Pwb16)
    TFc2c1.next.append(Pwc18)

    TFd4a3.pre.append(Pd4a3)
    TFa4b3.pre.append(Pa4b3)
    TFb4c3.pre.append(Pb4c3)
    TFc4d3.pre.append(Pc4d3)
    TFd4a3.next.append(Pwa37)
    TFa4b3.next.append(Pwb36)
    TFb4c3.next.append(Pwc38)
    TFc4d3.next.append(Pwd35)

    Pwa37.next.append(Ta37)
    Pwb36.next.append(Tb36)
    Pwc38.next.append(Tc38)
    Pwd35.next.append(Td35)

    Ta37.pre.append(Pwa37)
    Tb36.pre.append(Pwb36)
    Tc38.pre.append(Pwc38)
    Td35.pre.append(Pwd35)
    Ta37.next.append(Pa3)
    Tb36.next.append(Pb3)
    Tc38.next.append(Pc3)
    Td35.next.append(Pd3)

    def target5(self):
        count = 0
        for node in self.Go5:
            count += node.token
        return count

    def target6(self):
        count = 0
        for node in self.Go6:
            count += node.token
        return count

    def target7(self):
        count = 0
        for node in self.Go7:
            count += node.token
        return count

    def target8(self):
        count = 0
        for node in self.Go8:
            count += node.token
        return count

    def target5l(self):
        count = 0
        for node in self.Go5l:
            count += node.token
        return count

    def target6l(self):
        count = 0
        for node in self.Go6l:
            count += node.token
        return count

    def target7l(self):
        count = 0
        for node in self.Go7l:
            count += node.token
        return count

    def target8l(self):
        count = 0
        for node in self.Go8l:
            count += node.token
        return count

    def getCarInIntersection(self):
        cars = [self.target5(), self.target5l(), self.target6(), self.target6l(), self.target7(), self.target7l(),
                self.target8(), self.target8l()]
        return cars

    def roadControl(self, cars):
        self.carNums = [self.target5(), self.target5l(), self.target6(), self.target6l(), self.target7(),
                        self.target7l(), self.target8(), self.target8l()]

        for car in cars:
            # print(car.events[len(car.events) - 2])
            if car.events[len(car.events) - 2] == 'Td15':
                self.carNums[0] += 1
            elif car.events[len(car.events) - 2] == 'Td35':
                self.carNums[1] += 1
            elif car.events[len(car.events) - 2] == 'Tb16':
                self.carNums[2] += 1
            elif car.events[len(car.events) - 2] == 'Tb36':
                self.carNums[3] += 1
            elif car.events[len(car.events) - 2] == 'Ta17':
                self.carNums[4] += 1
            elif car.events[len(car.events) - 2] == 'Ta37':
                self.carNums[5] += 1
            elif car.events[len(car.events) - 2] == 'Tc18':
                self.carNums[6] += 1
            elif car.events[len(car.events) - 2] == 'Tc38':
                self.carNums[7] += 1
        # print(self.carNums)
