class Place:
    def __init__(self, pname, token=0):
        self.type = 1  # 1=place
        self.token = token
        self.next = []
        self.pname = pname


class RoadPlace:
    def __init__(self, pname, token=1):
        self.type = 2  # 路权
        self.token = token
        self.pname = pname


class Transition:
    def __init__(self, name, wait=0):
        self.type = 3
        self.pre = []
        self.next = []
        self.wait = wait
        self.name = name


class TimedTransition:
    def __init__(self, name, duration, end=0, wait=0):
        self.type = 4
        self.pre = []
        self.next = []
        self.duration = duration
        self.end = end
        self.name = name
        self.wait = wait


class TransitionWithInhibitArc:  # 带抑止弧的变迁
    def __init__(self, name, wait=0):
        self.type = 5
        self.pre = []
        self.prex = []
        self.next = []
        self.wait = wait
        self.name = name


class PrePost:
    def __init__(self, pre, post, name):
        self.name = name
        self.pre = pre
        self.post = post