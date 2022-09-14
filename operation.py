# import Setting as st
from Car import Car
from place import PrePost


def arriveRe(cars, screen, InR, carsH):
    for In in InR:
        if In != 0:
            car = Car(screen, In)
            car.curevent = 1  # 初始话车辆
            cars.append(car)
            carsH.append(car)


def writeM(M, PN):  # 写入状态
    for i in range(len(PN.PNodes)):
        PN.PNodes[i].token = M[i]


def CurM(PN):  # 当前状态
    M = []
    for node in PN.PNodes:
        M.append(node.token)
    return M


def canhappen(curnode):  # 变迁是否可以发生
    fmark = False  # 发生标志
    if curnode == None:
        return True
    if curnode.type == 3 or curnode.type == 4:  # 普通与时间变迁
        condition = len(curnode.pre)  # 发生条件
        count = 0
        if len(curnode.pre) != 0:  # 如果有节点
            for node in curnode.pre:  # 对所有place 满足所有发生条件
                if node.token >= 1:  # 有token
                    count += 1
            if count == condition:  # 满足发生条件
                fmark = True
        else:
            fmark = True

        for node in curnode.next:  # place max =1
            if node.token >= 1:
                fmark = False

    if curnode.type == 5:
        fmark = True
        if curnode.pre[0].token == 0:  # place中是否有token
            fmark = False
        for node in curnode.prex:  # 约束弧前的place是否有token
            if node.token >= 1:
                fmark = False
                break
        for node in curnode.next:  # 约束弧后也不能有token
            if node.token >= 1:
                fmark = False
                break
    return fmark


def transition(node):  # 迁移函数
    if node == None:
        return True
    if canhappen(node):  # 是否可以发生
        for node1 in node.pre:
            node1.token -= 1
        for node2 in node.next:
            node2.token += 1
        return True
    return False


def canhappenStrict(PN, node):
    Mpre = CurM(PN)
    if node in PN.Tleave:
        return False

    if canhappen(node):  # 是否能够发生
        transition(node)
    else:
        return False

    if isdead(PN, Mpre):  # 发生后是否不死锁
        return False
    else:
        return True


def finish(PN):  # 把可以发生的时间变迁 都发生了 查看是否会死锁
    for node in PN.TNodes:
        if canhappen(node):
            transition(node)


def isdead(PN, M):
    finish(PN)
    #
    #
    # if PN.Pwa4b4.token== 1  and PN.Pwc4d4.token== 1 and PN.Pwb4c4.token== 1 and PN.Pwd2d4.token == 1 and PN.Pwa3d2.token== 1:
    #     writeM(M, PN)
    #     return True
    # if PN.Pwa4b4.token == 1 and PN.Pwc4d4.token == 1 and PN.Pwb2b4.token == 1and PN.Pwd4a4.token == 1 and PN.Pwc3b2.token== 1:
    #     writeM(M, PN)
    #     return True
    # if PN.Pwa4b4.token == 1 and PN.Pwc2c4.token == 1 and PN.Pwb4c4.token == 1 and PN.Pwd4a4.token == 1 and PN.Pwd3c2.token== 1:
    #     writeM(M, PN)
    #     return True
    # if PN.Pwa2a4.token == 1 and PN.Pwc4d4.token == 1 and PN.Pwb4c4.token == 1 and PN.Pwd4a4.token == 1 and PN.Pwb3a2.token== 1:
    #     writeM(M, PN)
    #     return True

    # if PN.Pwc1c3.token == 1 and PN.Pwc3b2.token == 1 and PN.Pwb2e.token == 1 and PN.Pwed3.token == 1 and PN.Pwd3c2.token == 1 and PN.Pwc2c1.token == 1:
    #     writeM(M, PN)
    #     return True

    nodeList = []
    nodeName = []

    for node in PN.PPNodes:
        if node.token == 1:
            if "e" not in node.pname:
                nodeList.append(PrePost(node.pname[2:4], node.pname[4:6], node.pname[2:6]), )
                nodeName.append(node.pname[2:6])
            elif node.pname[4:5] == "e":
                nodeList.append(PrePost(node.pname[2:4], node.pname[4:5], node.pname[2:6]))
                nodeName.append(node.pname[2:5])
            elif node.pname[2:3] == "e":
                nodeList.append(PrePost(node.pname[2:3], node.pname[3:5], node.pname[2:6]))
                nodeName.append(node.pname[2:5])

    for i in range(0, len(nodeList)):
        endPoint = nodeList[i].pre
        startPoint = nodeList[i].post
        j = 0
        # loop = 0
        inLoop = []
        while j < len(nodeList):
            if nodeList[j].pre == startPoint and j not in inLoop:
                startPoint = nodeList[j].post
                inLoop.append(j)
                if startPoint == endPoint:
                    writeM(M, PN)
                    return True
                j = 0
                continue
            j += 1

    writeM(M, PN)
    return False
