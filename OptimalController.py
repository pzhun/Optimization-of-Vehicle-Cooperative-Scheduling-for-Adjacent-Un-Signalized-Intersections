import operation as op
import Car_Function as cf
import Car_Move as CM
class Node():
    def __init__(self,marking,sequence):
        self.marking = marking[:]
        self.sequence = sequence[:]

def OptiamlSequence(cars, PN):
    Mref = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    optiamlSequence = []
    carEvents = []
    # case = 0
    M_0 = op.CurM(PN)
    level = [[Node(M_0,[])]]
    for car in cars:
        event = car.events[car.curevent]
        if car.curevent>=1 and event!="out" and event not in carEvents and "F" not in event:
            carEvents.append(event)
    feasibleSequences = []
    # print(carEvents)

    for i in range(0,len(carEvents)):
        level.append([])
        n = 0
        for node in level[i]:# 该node 表示上一层的每个节点
            op.writeM(node.marking, PN) #以该节点的状态为初始状态
            feasibleNodes = feasibleNode(node.marking,carEvents, PN)
            if len(feasibleNodes)==0:
                feasibleSequences.append(node.sequence)
            if n>5000:
                break
            for feasNode in feasibleNodes:# 即将发生的所有可行解
                n += 1
                # print(n)
                op.transition(feasNode)
                sequence = node.sequence[:] # 继承上一层的序列，
                sequence.append(feasNode.name) #加入该事件
                level[i+1].append(Node(op.CurM(PN),sequence))
                if i == len(carEvents)-1 or op.CurM(PN)== Mref:
                    feasibleSequences.append(sequence)
                    if PN.GreedMark:
                        return sequence
                    # print(len(feasibleSequences))
                op.writeM(node.marking,PN) #回到初始状态，进行下次迭代

    # print("feasibleSequences", feasibleSequences)
    max=0
    for sequence in feasibleSequences:
        if len(sequence)>max:
            optiamlSequence = sequence[:]
            max = len(sequence)

    return optiamlSequence

def opt2ActionOptimal(Cars,sequence,PN):
    for car in Cars:  # 车辆有其对应的事件 且为瞬时事件
        event = car.events[car.curevent]
        # print(car.rect.centerx, car.rect.centery, car.row)
        if 'F' not in event:
            if event in sequence:
                node = findNode(PN, event)
                if node != None:
                    if op.canhappenStrict(PN, node):
                        op.transition(node)
                        CM.action(car, event)
                        car.curevent += 1
        else:
            CM.action_c(car, event)

def feasibleNode(M, events, PN):
    feaNodes=[]
    for event in events:
        if cf.pController(PN,event,M):
            feaNodes.append(findNode(PN,event))
        op.writeM(M, PN)
    return feaNodes

def findNode(PN, event):
    for node in PN.Nodes:  # 找到PN中对应的事件，如果可以发生 让其发生
        if node.name == event:
            return node


def greedController(cars_T,cars, PN):
    # Mref = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for car in cars_T:
        event = car.events[car.curevent]
        M = op.CurM(PN)
        if cf.pController(PN,event,M):
            cars.append(car)




